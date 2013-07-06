from django.db import models


class Setting(models.Model):
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.key + ': ' + self.value

    class Meta:
        db_table = 'websettings_setting'
