from websettings.backends import backend_module


class SettingStoreMetaClass(type):
    def __new__(cls, name, bases, attrs):
        p = super(SettingStoreMetaClass, cls)
        if name == 'SettingStore':
            return p.__new__(cls, name, bases, attrs)
        module = attrs.pop('__module__')
        new_class = p.__new__(cls, name, bases, {'__module__': module})
        new_class.settings = attrs.copy()

        return new_class


class SettingStore(object):
    __metaclass__ = SettingStoreMetaClass

    def __getattr__(self, item):
        if item not in self.settings.keys():
            raise AttributeError
        try:
            attr = backend_module.getsetting(item)
        except AttributeError:
            attr = self.settings[item]
        return attr

    def __setattr__(self, key, value):
        if key not in self.settings.keys():
            raise AttributeError
        backend_module.setsetting(key, value)
