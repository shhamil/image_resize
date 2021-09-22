import os.path
import urllib
from PIL import Image as Img
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PikchaListSerializer, PikchaDetailSerializer
from ..models import Pikcha
from ..utilities import resize_picture


class PikchaListApiView(APIView):
    def get(self, request):
        pictures = Pikcha.objects.all()
        serializer = PikchaListSerializer(pictures, many=True)
        return Response(serializer.data)

    def post(self, request):
        if "url" in request.POST.keys() and request.POST.get("url") is not None and request.POST.get("url") != "":
            pikcha = Pikcha()
            pikcha.url = request.POST.get("url")
            pikcha.save()

        elif "file" in request.POST.keys() and request.POST.get("file") is not None and request.POST.get("file") != "":
            pikcha = Pikcha()
            pikcha.file = request.POST.get("file")
            pikcha.save()
        return Response({"url": request.POST.get("url"), "file": request.POST.get("file")}, status=201)


class PikchaDetailView(APIView):

    def get(self, request, pk):
        picture = Pikcha.objects.get(pk=pk)
        serializer = PikchaDetailSerializer(picture)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        question = get_object_or_404(Pikcha, pk=kwargs['pk'])
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


class PikchaResizeView(APIView):
    def post(self, request, *args, **kwargs):
        image = Pikcha.objects.get(pk=kwargs['pk'])

        if "width" in request.POST.keys() \
                and request.POST.get("width") is not None\
                and request.POST.get("width") != "":
            width = request.POST.get("width")
            height = image.path_to_image.height
            width_for_name = request.POST.get("width")
            height_for_name = 0
            resize_picture(image, width, height, width_for_name, height_for_name)

        elif "height" in request.POST.keys() \
                and request.POST.get("height") is not None\
                and request.POST.get("height") != "":
            extension = str(image.path_to_image.path).split('.')[-1]
            width = image.path_to_image.width
            height = request.POST.get("height")
            width_for_name = 0
            height_for_name = request.POST.get("height")
            resize_picture(image, width, height, width_for_name, height_for_name)
        elif ("width" in request.POST.keys()
            and request.POST.get("width") is not None
            and request.POST.get("width") != "")\
                and ("height" in request.POST.keys()
                     and request.POST.get("height") is not None
                     and request.POST.get("height") != ""):
            extension = str(image.path_to_image.path).split('.')[-1]
            width = request.POST.get("width")
            height = request.POST.get("height")
            width_for_name = request.POST.get("width")
            height_for_name = request.POST.get("height")
            resize_picture(image, width, height, width_for_name, height_for_name)
        else:
            return Response("Некорректный запрос", status=status.HTTP_400_BAD_REQUEST)
        return Response({"width": request.POST.get("width")}, status=status.HTTP_201_CREATED)

