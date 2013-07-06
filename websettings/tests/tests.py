from django.test import TestCase


__all__ = (
    'DBSettingStoreTest',
)


class DBSettingStoreTest(TestCase):
    def makeOne(self):
        from websettings import websettings
        return websettings

    def test_get(self):
        store = self.makeOne()
        self.assertEqual(store.TEST_SETTING, 'before')

    def test_get_with_db(self):
        from websettings.models import Setting
        Setting.objects.create(key='TEST_SETTING', value='after')
        store = self.makeOne()
        self.assertEqual(store.TEST_SETTING, 'after')
