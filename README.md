# Python Flask Sample App

This is a python/flask app in order to provide a simple example. This example provides a frontend using HTML + CSS + Vanilla Javascript and a backend using Python + Flask.

!(https://raw.githubusercontent.com/acoronadoc/python-flask-sample/main/sample.png)

## API

- '/'(GET) Frontend Webapp.
- '/upload_image'(GET) Returns an simple html form to image uploads.
- '/upload_image'(POST) Uploads and check image format. If 'url'(String) paramter is present, the image will be download from that URL. If 'file'(File) parameter is present, the file will be uploaded. Just 'url' or 'file' are mandatory.
- '/list_images'(GET) Returns a JSON list of images. Each register contains an 'id'(Image unique Id) and 'name'(Image name).
- '/analyse_image/<uuid>'(GET) Returns a JSON Object width image name, image width and image height information.
   


