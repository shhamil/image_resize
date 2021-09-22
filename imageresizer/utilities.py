import os
import shutil

from PIL import Image as Img
from .models import Pikcha


def resize_picture(image, width, height, width_for_name, height_for_name):
    extension = str(image.path_to_image.path).split('.')[-1]
    output_size = (int(width), int(height))
    new_picture_name = image.name + '_' + str(width_for_name) + '_' + str(height_for_name) + "." + extension
    new_image = Pikcha.objects.create(name=new_picture_name,
                                      parent_picture=image.pk,
                                      )
    shutil.copy(image.path_to_image.path, os.path.dirname(image.path_to_image.path) + '\\' + new_picture_name)
    new_image.path_to_image = new_picture_name
    new_image.path_to_image.name = new_picture_name
    new_image.url = image.url
    new_image.path_to_image.open()
    imag = Img.open(new_image.path_to_image)
    imag.thumbnail(output_size)
    imag.save(new_image.path_to_image.path)
    new_image.width = new_image.path_to_image.width
    new_image.height = new_image.path_to_image.height
    new_image.picture = 'http://localhost:8000' + new_image.path_to_image.url
    new_image.save()
    imag.close()
