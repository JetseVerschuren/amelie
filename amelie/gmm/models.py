from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class GMM(models.Model):
    date = models.DateField(blank=True, null=True)
    agenda = RichTextUploadingField()

    def __str__(self):
        return self.date.__str__()

    class Meta:
        verbose_name = "GMM"
        verbose_name_plural = "GMMs"
        ordering = ["-date"]
