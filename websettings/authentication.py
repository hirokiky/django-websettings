from django.conf import settings
from django.shortcuts import redirect


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(settings.LOGIN_URL)

    return wrapper
