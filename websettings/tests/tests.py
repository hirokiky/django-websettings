from django.test import TestCase


__all__ = (
    'DBSettingStoreTest',
)


class DBSettingStoreTest(TestCase):
    def makeOne(self):
        from websettings.tests.settingstore import MySettingStore
        return MySettingStore

    def test_get(self):
        store_class = self.makeOne()
        store = store_class()
        self.assertEqual(store.TEST_SETTING, 'before')

    def test_get_with_db(self):
        from websettings.models import Setting
        store_class = self.makeOne()
        Setting.objects.create(key='TEST_SETTING', value='after')
        store = store_class()
        self.assertEqual(store.TEST_SETTING, 'after')
