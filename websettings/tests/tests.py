from django.test import TestCase


__all__ = (
    'DBBackendTest',
    'DBSettingStoreTest',
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
