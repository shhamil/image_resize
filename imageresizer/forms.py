from django import forms
from django.core.exceptions import ValidationError
from .models import Pikcha
from PIL import Image as Img
from urllib.request import urlopen
from .utilities import resize_picture


class ImageCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageCreateForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = "Введите url к картинке"
        self.fields['path_to_image'].label = "или выберите картинку"

    def clean(self):
        super().clean()
        try:
            pict = Img.open(urlopen(self.cleaned_data['url']))
        except:
            raise ValidationError('Это не картинка!')

    class Meta:
        model = Pikcha
        fields = ('url', 'path_to_image')


class ImageUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.pk_image = kwargs.pop('image_pk', None)
        super(ImageUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        image = Pikcha.objects.get(pk=self.pk_image)
        extension = str(image.path_to_image.path).split('.')[-1]
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        width_for_name = self.cleaned_data['width']
        height_for_name = self.cleaned_data['height']
        if self.cleaned_data['width'] == None or self.cleaned_data['width'] == 0:
            width_for_name = 0
            width = image.width
        elif self.cleaned_data['height'] == None or self.cleaned_data['height'] == 0:
            height_for_name = 0
            height = image.height

        output_size = (width, height)
        new_picture_name = image.name + '_' + str(width_for_name) + '_' + str(height_for_name) + "." + extension
        new_image = Pikcha.objects.create(name=new_picture_name,
                                          parent_picture=image.pk,
                                          )

        new_image.path_to_image.save(new_picture_name, image.path_to_image)
        new_image.url = image.url
        new_image.picture = 'http://localhost:8000' + new_image.path_to_image.url
        imag = Img.open(new_image.path_to_image.path)
        imag.thumbnail(output_size)
        imag.save(new_image.path_to_image.path)
        imag.close()
        return new_image

    class Meta:
        model = Pikcha
        fields = ('width', 'height')
