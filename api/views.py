# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import thread
import logging
import os

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)


@api_view(['GET'])
def img_list(request):
    media_dir = os.listdir(os.path.join(settings.BASE_DIR, 'media'))
    img_files = []
    return Response({"status": "Success", "message": "test"},
                    status=status.HTTP_200_SUCCESS)


@api_view(['GET'])
def img_detail(request):
    import pdb
    pdb.set_trace()
    media_dir = os.listdir(os.path.join(settings.BASE_DIR, 'media'))
    # if file_name in media_dir:
    #     return Response(file_name, content_type="image/png")
    pass


@api_view(['POST', 'PATCH'])
def img_patch(request):
    path = os.path.join(settings.UPLD_DIR, str(Binary_Data.Image))
    result = os.remove(str(path))


@api_view(['POST', 'DELETE'])
def img_delete(request):
    path = os.path.join(settings.UPLD_DIR, str(Binary_Data.Image))
    result = os.remove(str(path))


@api_view(['POST'])
def img_upload(request):
    """
    :param request: curl http://127.0.0.1:7000/img_upload/
                    -H 'Authorization: Token 83ad3234729c4b3c03b32a75297444d64761e359'
                    -H 'Content-Type: multipart/form-data'
                    -F 'img_file=@/Users/../Desktop/lambho.jpg'
    :return: {
              "status": "Created",
              "message": "Image uploaded successfully and stored in MEDIA_ROOT",
            }
    """
    import pdb
    pdb.set_trace()
    try:
        if request.FILES:
            os.mkdir(os.path.join(settings.BASE_DIR, 'media', request.auth.key))
            file_obj = request.FILES['img_file']
            filename = file_obj.name

            with default_storage.open(os.path.join(request.auth.key, filename), 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
            # logger.info("API file_upload view, img file uploaded {}".format(filename))
            return Response({"status": "Success",
                     "message": "Image file uploaded successfully and stored in MEDIA_ROOT",
                     }, status=status.HTTP_201_CREATED)
    except Exception as e:
        print "api file_upload view : " + str(e)
        return Response({"status": "Failed", "error": "Internal Server Error"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)