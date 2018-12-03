# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import thread
import logging
import os

from django.core.files.storage import default_storage
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)

# API request to generate token using username and password [authorization API]
"""
Request: http POST http://127.0.0.1:9090/api/api-token-auth/ username='' password=''
Response:
{
    "token": "......."
}
"""


@api_view(['GET'])
def img_list(request):
    """
    :param request: curl -X GET -H 'Content-Type:application/json'
                                -H 'Authorization: Token 83ad3234729c4b3c03b32a75297444d64761e359
                                http://127.0.0.1:7000/img_list/
    :return: {"status":"Success","images":["lambho.jpg"]}
    """
    try:
        img_files_list = os.listdir(os.path.join(settings.BASE_DIR, 'media', request.auth.key))
        if img_files_list:
            return Response({"status": "Success", "images": img_files_list},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "Failed", "error": "No files found"},
                            status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print "api img_list view : " + str(e)
        return Response({"status": "Failed", "error": e},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def img_detail(request):
    # import pdb
    # pdb.set_trace()
    media_dir = os.listdir(os.path.join(settings.BASE_DIR, 'media', request.auth.key))
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
    :param request: curl -X POST http://127.0.0.1:7000/img_upload/
                    -H 'Authorization: Token 83ad3234729c4b3c03b32a75297444d64761e359'
                    -H 'Content-Type: multipart/form-data'
                    -F 'img_file=@/path_to_img_file/test.jpg'
    :return: {
              "status": "Created",
              "message": "Image uploaded successfully and stored in MEDIA_ROOT",
            }
    """
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
        else:
            return Response({"status": "Failed", "error": "img_file value cannot be empty"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        print "api file_upload view : " + str(e)
        return Response({"status": "Failed", "error": e},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
