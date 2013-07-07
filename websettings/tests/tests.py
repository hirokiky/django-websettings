from django.test import TestCase, RequestFactory


__all__ = (
    'AdminRequiredTest',
    'DBBackendTest',
    'DBSettingStoreTest',
    'SettingStoreTest',
)


class DBBackendTest(TestCase):
    def _getTarget(self):
        from websettings.backends import db
        return db

    def _set_setting(self, **kwargs):
        from websettings.models import Setting
        return Setting.objects.create(**kwargs)

    def _get_setting(self, **kwargs):
        from websettings.models import Setting
        return Setting.objects.get(**kwargs)

    def test_getsetting_with_setting(self):
        self._set_setting(key='BOSS', value='ritsu')
        target = self._getTarget()
        result = target.getsetting('BOSS')
        self.assertEqual('ritsu', result)

    def test_getsetting_without_setting(self):
        target = self._getTarget()
        self.assertRaises(AttributeError, target.getsetting, 'BOSS')

    def test_setsetting_with_setting(self):
        self._set_setting(key='BOSS', value='ritsu')
        target = self._getTarget()
        target.setsetting('BOSS', 'mio')

        result = self._get_setting(key='BOSS')
        self.assertEqual(result.value, 'mio')

    def test_setting_without_setting(self):
        target = self._getTarget()
        target.setsetting('BOSS', 'ritsu')

        result = self._get_setting(key='BOSS')
        self.assertEqual(result.value, 'ritsu')


class AdminRequiredTest(TestCase):
    def _getTarget(self):
        from websettings.authentication import admin_required
        return admin_required

    def _makeOne(self):
        def dummy(request):
            return 'dummy response'
        target = self._getTarget()
        return target(dummy)

    def _get_request(self, *args, **kwargs):
        rf = RequestFactory()
        return rf.get(*args, **kwargs)

    def test_it_with_staff(self):
        from django.contrib.auth.models import User
        target = self._makeOne()
        req = self._get_request(path='/test/')
        req.user = User(username='dummy', is_staff=True)
        result = target(req)
        self.assertEqual('dummy response', result)

    def test_it_with_anonymous(self):
        from django.contrib.auth.models import AnonymousUser
        target = self._makeOne()
        req = self._get_request(path='/test/')
        req.user = AnonymousUser()
        with self.settings(LOGIN_URL='/dummy/'):
            result = target(req)
            self.assertEqual(result['Location'], '/dummy/')


class SettingStoreTest(TestCase):
    def _getTarget(self):
        from websettings.base import SettingStore
        return SettingStore

    def _makeOne(self, backend_module):
        target_class = self._getTarget()
        target = target_class()
        target.backend_module = backend_module
        return target

    def test_getattr(self):
        class Dummy(object):
            def getsetting(self, item):
                return item
        target = self._makeOne(Dummy())
        target.settings = {'DRUM': 'before'}
        self.assertEqual(target.DRUM, 'DRUM')

    def test_setattr(self):
        store = {}

        class Dummy(object):
            potal = store

            def setsetting(self, key, value):
                self.potal[key] = value
        target = self._makeOne(Dummy())
        target.settings = {'DRUM': 'before'}
        target.DRUM = 'ritsu'
        self.assertEqual(store['DRUM'], 'ritsu')


class DBSettingStoreTest(TestCase):
    def _getTarget(self):
        from websettings import websettings
        return websettings

    def test_get(self):
        target = self._getTarget()
        self.assertEqual(target.TEST_SETTING, 'before')

    def test_get_with_db(self):
        from websettings.models import Setting
        Setting.objects.create(key='TEST_SETTING', value='after')
        target = self._getTarget()
        self.assertEqual(target.TEST_SETTING, 'after')
