# Python Flask Sample App

This is a python/flask app in order to provide a simple example. This example provides a frontend using HTML + CSS + Vanilla Javascript and a backend using Python + Flask.

![Screenshot](https://raw.githubusercontent.com/acoronadoc/python-flask-sample/main/sample.png)

## Run application

```
# Create and activate the environment (Linux)
virtualenv env
source env/bin/activate

# Install python dependencies
pip install -r requirements.txt

# Run application
flask run
```

## API

- '/'(GET) Frontend Webapp.
- '/upload_image'(GET) Returns an simple html form to image uploads.
- '/upload_image'(POST) Uploads and check image format. If 'url'(String) paramter is present, the image will be download from that URL. If 'file'(File) parameter is present, the file will be uploaded. Just 'url' or 'file' are mandatory.
- '/list_images'(GET) Returns a JSON list of images. Each register contains an 'id'(Image unique Id) and 'name'(Image name).
- '/analyse_image/<uuid>'(GET) Returns a JSON Object width image name, image width and image height information.
   
## App files
   
- 'requirements.txt' Contains Python requirements.
- 'app.py' Is the main file of the aplication. Contains all Python/Flask code with the API.
- '/static' Is the static files folder. Contains a CSS file(main.css) with the styles of the aplication(fonts, colors, ...) and a JS file(main.js) with all vanilla Javascript code.
- '/templates' Contains all Jinja 2 templates. The index.html is used in order to render the main webapp and the upload.html is used in order to render a simple HTML form.
- '/data' This folder is used to store al application data(Ids and images).
 
