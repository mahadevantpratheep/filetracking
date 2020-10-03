from django.db import models


class Permission(models.Model):
    evnt_name = models.CharField(max_length=200)
    myfile = models.FileField(upload_to='documents/%Y/%m/%d',
                              default="documents/defimage.jpg")
    accepted = models.BooleanField(default=False)
    description = models.TextField(blank=False)
    status = models.TextField(default="Pending")

    def __str__(self):
        return self.evnt_name
