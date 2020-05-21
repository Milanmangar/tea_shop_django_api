from django.db import models
from datetime import datetime
import uuid
import os


def blog_image_file_path(instance, filename):
    """ generate file path for new image for item """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/blog/', filename)


class Items(models.Model):
    added_by = models.CharField(max_length=256, default="owner")
    image = models.ImageField(upload_to=blog_image_file_path)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=False, default="")
    added_date = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=50, blank=False, default='active')

    def __str__(self):
        return f'"{self.name}" added by {self.added_by}'
