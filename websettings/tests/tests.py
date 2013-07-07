from django.test import TestCase


__all__ = (
    'DBSettingStoreTest',
)


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
