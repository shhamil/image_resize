import shutil

from django.db import models
from django.core.files import File
from PIL import Image as Img
import urllib.request
import os



class Pikcha(models.Model):
    class Meta:
        db_table = 'Images'

    name = models.TextField(blank=True, verbose_name='Имя файла')
    file = models.TextField(blank=True)
    url = models.URLField(blank=True, verbose_name='url к картинке для загрузки с указанного url')
    width = models.PositiveIntegerField(verbose_name='Ширина', default=0)
    height = models.PositiveIntegerField(verbose_name='Высота', default=0)
    path_to_image = models.ImageField(blank=True)
    picture = models.CharField(max_length=255)
    parent_picture = models.IntegerField(verbose_name='Исходная картинка', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.url and not self.path_to_image and not self.file:
            image_file = urllib.request.urlretrieve(self.url)
            self.path_to_image.save(os.path.basename(self.url), File(open(image_file[0], 'rb')))
            self.width = self.path_to_image.width
            self.height = self.path_to_image.height
            self.picture = 'http://localhost:8000' + self.path_to_image.url
            self.name = os.path.basename(self.url)
        if self.file and not self.path_to_image and not self.url:
            shutil.copy(self.file, './media/')
            self.path_to_image = (os.path.basename(self.file))
            self.width = self.path_to_image.width
            self.height = self.path_to_image.height
            self.picture = 'http://localhost:8000' + self.path_to_image.url
            self.name = os.path.basename(self.file)
        super(Pikcha, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

