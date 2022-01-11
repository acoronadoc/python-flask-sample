from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from PIL import Image
import io
import os
import requests
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET'] )
def index():
    return render_template("index.html")
    
@app.route('/list_images', methods=['GET'] )
def listImages():
    images = []
    listUIDs = os.listdir( os.path.join(os.getcwd(), "data") )
    
    for uid in listUIDs:
       reg = { "id": uid, "name": "" }
       files = os.listdir( os.path.join(os.getcwd(), "data", uid) )
       if len(files)>=1:
           reg["name"]=files[0]
       
       images.append(reg)
    
    return jsonify(images)

@app.route('/upload_image', methods=['GET', 'POST'])
def uploadImage():
    if request.method == 'GET':
         return render_template("upload.html")
         
    url=request.form.get('url', default = '', type = str)
    filename=""
    
    if url!="":
      response = requests.get( url )
      fileUpload = io.BytesIO(response.content)
      filename=os.path.basename( url )
    else:
      fileUpload = request.files['file']
      filename=fileUpload.filename
    try:
       im=Image.open(fileUpload)

       fileId=str( uuid.uuid1() );
       os.mkdir( os.path.join(os.getcwd(), "data", fileId ) )
    
       im.save( os.path.join(os.getcwd(), "data", fileId, filename ) )
    except IOError:
       return 'bad image format!', 400

    return redirect(url_for('index'))
    

@app.route('/analyse_image/<uuid>')
def analyseImage(uuid):
    name=""
    width=""
    height=""
    
    files = os.listdir( os.path.join(os.getcwd(), "data", uuid) )
    if len(files)>=1:
       name=files[0]
    
       img  = Image.open( os.path.join(os.getcwd(), "data", uuid, name) )
       width, height = img.size

    return jsonify( { "name": name, "width": width, "height": height, "uuid": uuid } )
    
@app.route('/download/<uuid>/<filename>')
def download(uuid, filename):
	uploads = os.path.join(os.getcwd(), "data", uuid)
	return send_from_directory( uploads, filename)
	
