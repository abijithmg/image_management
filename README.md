# image_management 

- SETUP:
  - mkdir workspace
  - cd workspace
  - virtualenv IMG_ENV
  - IMG_ENV/bin/activate
  - git clone https://github.com/abijithmg/image_management.git
  - cd image_management
  - pip install -r requirements.txt
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py drf_create_token
  - mkdir media

- API requests:

  - Image upload:
    curl -X POST http://127.0.0.1:7000/img_upload/ -H 'Authorization: Token _token_' -H 'Content-Type: multipart/form-data' -F 'img_file=@/path_to_img_file/test.jpg'
  - Image list:
    curl -X GET -H 'Content-Type:application/json'
                                -H 'Authorization: Token 83ad3234729c4b3c03b32a75297444d64761e359
                                http://127.0.0.1:7000/img_list/


- NOTE: DB is used only to make access tokens persistent and no meta data of images are being stored in the DB
