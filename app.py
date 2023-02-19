from flask import Flask,render_template,request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app=Flask(__name__)
model=load_model('riceDisease.h5')



def modelPrediction(imagePath):
    img=image.load_img(imagePath,target_size=(224,224))
    img=image.img_to_array(img)/255
    x=np.expand_dims(img,0)
    pre=model.predict(x)#[3]
    pre=pre[0]
    if pre>0.5:
        return 'Healthy'
    else:
        return 'Diseased'

    
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        imag=request.files['my_image']
        imagPath='static/'+imag.filename
        imag.save(imagPath)
        prediction=modelPrediction(imagPath)
        return render_template('predict.html',prediction=prediction,imag_path=imagPath)

if __name__=='__main__':
    app.run(debug=True)
