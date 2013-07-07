from functools import partial

from django import forms
from django.utils.datastructures import SortedDict

from websettings import websettings


def get_settingstore_fields():
    fields = [(k, forms.CharField(max_length=255,
                                  label=k,
                                  initial=partial(getattr, websettings, k)))
              for k in websettings.settings.keys()]
    return SortedDict(fields)


class SettingStoreFieldsMetaclass(type):
    def __new__(cls, *args, **kwargs):
        super_new = super(SettingStoreFieldsMetaclass, cls).__new__
        new_class = super_new(cls, *args, **kwargs)

        new_class.base_fields = get_settingstore_fields()
        return new_class


class BaseSettingStoreForm(forms.BaseForm):
    def save(self):
        if hasattr(self, 'cleaned_data'):
            for k, v in self.cleaned_data.items():
                setattr(websettings, k, v)
        else:
            # TODO: need more humanization.
            raise ValueError('Form needs cleaned_data')


class SettingStoreForm(BaseSettingStoreForm):
    __metaclass__ = SettingStoreFieldsMetaclass
