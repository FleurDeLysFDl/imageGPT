import replicate
import os
from PIL import Image
import requests
from flask import Flask,render_template,request

os.environ["REPLICATE_API_TOKEN"]="r8_KGgOCwTJvjWp0hJOUfiAr1SoCTGBWQQ2UahyC" 
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("describe")
        print(q)
        r = {"prompt":q}
        re = version.predict(**r)
        return (render_template("index.html",result=re[0]))
    else:
        return(render_template("index.html",result="waiting..."))

if __name__=="__main__":
    app.run()
