from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('predictor.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():

    site=np.zeros(96)
    if site=='Alandi Road':
            site[0]=1
    if site=='Ambegaon Budruk':
            site[1]=1
    if site=='Anandnagar':
            site[2]=1
    if site=='Aundh':
            site[3]=1
    if site=='Aundh Road':
            site[4]=1
    if site=='Balaji Nagar':
            site[5]=1
    if site=='Baner':
            site[6]=1
    if site=='Baner road':
            site[7]=1
    if site=='Alandi Road':
            site[8]=1
    if site=='Alandi Road':
            site[9]=1
    if site=='Alandi Road':
            site[10]=1
    if site=='Alandi Road':
            site[11]=1
    if site=='Alandi Road':
            site[12]=1
    if site=='Alandi Road':
            site[13]=1
    if site=='Alandi Road':
            site[14]=1
    if site=='Alandi Road':
            site[15]=1
    if site=='Alandi Road':
            site[16]=1
    if site=='Alandi Road':
            site[17]=1
    if site=='Alandi Road':
            site[18]=1
    if site=='Alandi Road':
            site[19]=1
    if site=='Alandi Road':
            site[20]=1
    if site=='Alandi Road':
            site[21]=1
    if site=='Alandi Road':
            site[22]=1
    if site=='Alandi Road':
            site[23]=1
    if site=='Alandi Road':
            site[24]=1
    if site=='Alandi Road':
            site[25]=1
    if site=='Alandi Road':
            site[26]=1
    if site=='Alandi Road':
            site[27]=1
    if site=='Alandi Road':
            site[28]=1
    if site=='Alandi Road':
            site[29]=1
    if site=='Alandi Road':
            site[30]=1
    if site=='Alandi Road':
            site[31]=1
    if site=='Alandi Road':
            site[32]=1
    if site=='Alandi Road':
            site[33]=1
    if site=='Alandi Road':
            site[34]=1
    if site=='Alandi Road':
            site[35]=1
    if site=='Alandi Road':
            site[36]=1
    if site=='Alandi Road':
            site[37]=1
    if site=='Alandi Road':
            site[38]=1
    if site=='Alandi Road':
            site[39]=1
    if site=='Alandi Road':
            site[40]=1
    if site=='Alandi Road':
            site[41]=1
    if site=='Alandi Road':
            site[42]=1
    if site=='Alandi Road':
            site[43]=1
    if site=='Alandi Road':
            site[44]=1
    if site=='Alandi Road':
            site[45]=1
    if site=='Alandi Road':
            site[46]=1
    if site=='Alandi Road':
            site[47]=1
    if site=='Alandi Road':
            site[48]=1
    if site=='Alandi Road':
            site[49]=1
    if site=='Alandi Road':
            site[50]=1
    if site=='Alandi Road':
            site[51]=1
    if site=='Alandi Road':
            site[52]=1
    if site=='Alandi Road':
            site[53]=1
    if site=='Alandi Road':
            site[54]=1
    if site=='Alandi Road':
            site[55]=1
    if site=='Alandi Road':
            site[56]=1
    if site=='Alandi Road':
            site[57]=1
    if site=='Alandi Road':
            site[58]=1
    if site=='Alandi Road':
            site[59]=1
    if site=='Alandi Road':
            site[60]=1
    if site=='Alandi Road':
            site[61]=1
    if site=='Alandi Road':
            site[62]=1
    if site=='Alandi Road':
            site[63]=1
    if site=='Alandi Road':
            site[64]=1
    if site=='Alandi Road':
            site[65]=1
    if site=='Alandi Road':
            site[66]=1
    if site=='Alandi Road':
            site[67]=1
    if site=='Alandi Road':
            site[68]=1
    if site=='Alandi Road':
            site[69]=1
    if site=='Alandi Road':
            site[70]=1
    if site=='Alandi Road':
            site[71]=1
    if site=='Alandi Road':
            site[72]=1
    if site=='Alandi Road':
            site[73]=1
    if site=='Alandi Road':
            site[74]=1
    if site=='Alandi Road':
            site[75]=1
    if site=='Alandi Road':
            site[76]=1
    if site=='Alandi Road':
            site[77]=1
    if site=='Alandi Road':
            site[78]=1
    if site=='Alandi Road':
            site[79]=1
    if site=='Alandi Road':
            site[80]=1
    if site=='Alandi Road':
            site[81]=1
    if site=='Alandi Road':
            site[82]=1
    if site=='Alandi Road':
            site[83]=1
    if site=='Alandi Road':
            site[84]=1
    if site=='Alandi Road':
            site[85]=1
    if site=='Alandi Road':
            site[86]=1
    if site=='Alandi Road':
            site[87]=1
    if site=='Alandi Road':
            site[88]=1
    if site=='Alandi Road':
            site[89]=1
    if site=='Alandi Road':
            site[90]=1
    if site=='Alandi Road':
            site[91]=1
    if site=='Alandi Road':
            site[92]=1
    if site=='Alandi Road':
            site[93]=1
    if site=='Alandi Road':
            site[94]=1
    if site=='Yerawada':
            site[95]=1

    # HTML -> .py
    if request.method == "POST":
        area = np.array([float(request.form["Land Area"])])
        bed = np.array([float(request.form["Bedrooms"])])
        bath = np.array([float(request.form["Bathrooms"])])
        bal = np.array([float(request.form["Balcony"])])

        site = request.form["Location"]

        data=np.concatenate([area,bath,bal,bed,site])
        prediction=int(model.predict([data])[0])

    #.py -> HTML    
    return render_template('predict.html', a = area, s = site, b1 = bed, b2 = bath, b3 = bal, predicted_value = prediction)

if __name__=="__main__":
    app.run(debug=True)