from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from websettings import websettings
from websettings.authentication import admin_required
from websettings.forms import SettingStoreForm


@require_http_methods(["GET"])
@admin_required
def list_view(request):
    return TemplateResponse(request,
                            'websettings/list.html',
                            dict(websettings=websettings))


@require_http_methods(["GET", "POST"])
@admin_required
def edit_view(request):
    if request.method == 'GET':
        form = SettingStoreForm()
    else:
        form = SettingStoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('websettings.views.list_view')

    return TemplateResponse(request,
                            'websettings/edit.html',
                            dict(form=form))
