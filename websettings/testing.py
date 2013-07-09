import websettings


class override_websettings(object):
    def __init__(self, **kwargs):
        self.options = kwargs
        self.tmp_settings = websettings.websettings.settings.copy()

    def __enter__(self):
        for k, v in self.options.items():
            websettings.websettings.settings[k] = v

    def __exit__(self, exc_type, exc_val, exc_tb):
        websettings.websettings.settings = self.tmp_settings
