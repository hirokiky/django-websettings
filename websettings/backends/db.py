from websettings.models import Setting


def getsetting(item):
    try:
        s = Setting.objects.get(key=item)
    except Setting.DoesNotExist:
        raise AttributeError

    return s.value


def setsetting(key, value):
    try:
        s = Setting.objects.get(key=key)
        s.value = value
        s.save()
    except Setting.DoesNotExist:
        Setting.objects.create(key=key,
                               value=value)
