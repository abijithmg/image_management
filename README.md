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

- API requests:

  - Image upload:
    curl http://127.0.0.1:7000/img_upload/ -H 'Authorization: Token _token_' -H 'Content-Type: multipart/form-data' -F 'img_file=@/path_to_img_file/test.jpg'
