from django.db import models


class Permission(models.Model):
    evnt_name = models.CharField(max_length=200)
    myfile = models.FileField(upload_to='documents/')
    accepted = models.BooleanField(default=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.evnt_name
