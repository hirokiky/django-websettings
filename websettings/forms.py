from functools import partial

from django import forms
from django.utils import six
from django.utils.datastructures import SortedDict

from websettings import websettings


def get_settingstore_fields(setting_store):
    fields = [(k, forms.CharField(max_length=255,
                                  label=k,
                                  initial=partial(getattr, setting_store, k)))
              for k in setting_store.settings.keys()]
    return SortedDict(fields)


class SettingStoreFieldsMetaclass(type):
    def __new__(cls, name, bases, attrs):
        super_new = super(SettingStoreFieldsMetaclass, cls).__new__
        new_class = super_new(cls, name, bases, attrs)

        setting_store = attrs.get('setting_store', websettings)
        new_class.base_fields = get_settingstore_fields(setting_store)
        return new_class


class BaseSettingStoreForm(forms.BaseForm):
    def save(self):
        if hasattr(self, 'cleaned_data'):
            for k, v in self.cleaned_data.items():
                setattr(self.setting_store, k, v)
        else:
            # TODO: need more humanization.
            raise ValueError('Form needs cleaned_data')


class SettingStoreForm(six.with_metaclass(SettingStoreFieldsMetaclass, BaseSettingStoreForm)):
    # For more testable
    setting_store = websettings
