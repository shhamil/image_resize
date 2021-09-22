from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from .models import Pikcha
from django.urls import reverse_lazy
from .forms import ImageCreateForm, ImageUpdateForm


class IndexView(ListView):
    """Главная страница"""
    model = Pikcha
    context_object_name = 'images'
    paginate_by = 4
    template_name = 'imageresizer/index.html'


class ImageCreateView(CreateView):
    """Страница загрузки новой картинки"""
    model = Pikcha
    form_class = ImageCreateForm
    success_url = reverse_lazy('imageresizer:index')
    template_name = 'imageresizer/create_images.html'


class ImageUpdateView(UpdateView):
    """Страница изменения размера картинки"""
    model = Pikcha
    form_class = ImageUpdateForm
    success_url = reverse_lazy('imageresizer:index')
    template_name = 'imageresizer/update_images.html'

    def get_form_kwargs(self):
        kwargs = super(ImageUpdateView, self).get_form_kwargs()
        kwargs['image_pk'] = self.kwargs['pk']
        print(self.kwargs['pk'])
        return kwargs
