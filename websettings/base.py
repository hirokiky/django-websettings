from django.conf import settings
from django.utils import six
from django.utils.importlib import import_module

from websettings.backends import backend_module


class SettingStoreMetaClass(type):
    def __new__(cls, *args, **kwargs):
        super_new = super(SettingStoreMetaClass, cls).__new__
        new_class = super_new(cls, *args, **kwargs)

        mod_path = settings.WEBSETTINGS_MODULE
        mod = import_module(mod_path)
        new_class.settings = {}

        for setting in dir(mod):
            if setting == setting.upper():
                setting_value = getattr(mod, setting)
                new_class.settings[setting] = setting_value

        return new_class


class SettingStore(six.with_metaclass(SettingStoreMetaClass, object)):
    # For more testable
    backend_module = backend_module

    def __getattr__(self, item):
        if item == item.upper():
            if item not in self.settings.keys():
                raise AttributeError
            try:
                attr = self.backend_module.getsetting(item)
            except AttributeError:
                attr = self.settings[item]
            return attr

    def __setattr__(self, key, value):
        if key == key.upper():
            if key not in self.settings.keys():
                raise AttributeError
            self.backend_module.setsetting(key, value)
        else:
            return super(SettingStore, self).__setattr__(key, value)

    def __iter__(self):
        for key in self.settings.keys():
            yield key, getattr(self, key)

    def __len__(self):
        return len(self.settings)

    def clear_trash(self):
        exclude_keys = list(self.settings)
        self.backend_module.exclude_clear(exclude_keys)
