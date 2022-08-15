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
        # area = request.form["Land Area"]
        # bed = request.form["Bedrooms"]
        # bath = request.form["Bathrooms"]
        # bal = request.form["Balcony"]
        # site = request.form["Location"]

        # loc_index = np.where(X.columns==site)[0][0]

        # x = np.zeros(len(X.columns))
        # x[0] = area
        # x[1] = bath
        # x[2] = bed
        # x[3] = bal
        # if loc_index >= 0:
        #         x[loc_index] = 1

        # return model.predict([x])[0]


    site_arr=np.zeros(96)

        # HTML -> .py
    if request.method == "POST":

        site = request.form["Location"]

        if site=='Alandi Road':
                site_arr[0]=1
        elif site=='Ambegaon Budruk':
                site_arr[1]=1
        elif site=='Anandnagar':
                site_arr[2]=1
        elif site=='Aundh':
                site_arr[3]=1
        elif site=='Aundh Road':
                site_arr[4]=1
        elif site=='Balaji Nagar':
                site_arr[5]=1
        elif site=='Baner':
                site_arr[6]=1
        elif site=='Baner road':
                site_arr[7]=1
        elif site=='Bhandarkar Road':
                site_arr[8]=1
        elif site=='Bhavani Peth':
                site_arr[9]=1
        elif site=='Bibvewadi':
                site_arr[10]=1
        elif site=='Bopodi':
                site_arr[11]=1
        elif site=='Budhwar Peth':
                site_arr[12]=1
        elif site=='Bund Garden Road':
                site_arr[13]=1
        elif site=='Camp':
                site_arr[14]=1
        elif site=='Chandan Nagar':
                site_arr[15]=1
        elif site=='Dapodi':
                site_arr[16]=1
        elif site=='Deccan Gymkhana':
                site_arr[17]=1
        elif site=='Dehu Road':
                site_arr[18]=1
        elif site=='Dhankawadi':
                site_arr[19]=1
        elif site=='Dhayari Phata':
                site_arr[20]=1
        elif site=='Dhole Patil Road':
                site_arr[21]=1
        elif site=='Erandwane':
                site_arr[22]=1
        elif site=='Fatima Nagar':
                site_arr[23]=1
        elif site=='Fergusson College Road':
                site_arr[24]=1
        elif site=='Ganesh Peth':
                site_arr[25]=1
        elif site=='Ganeshkhind':
                site_arr[26]=1
        elif site=='Ghorpade Peth':
                site_arr[27]=1
        elif site=='Ghorpadi':
                site_arr[28]=1
        elif site=='Gokhale Nagar':
                site_arr[29]=1
        elif site=='Gultekdi':
                site_arr[30]=1
        elif site=='Guruwar peth':
                site_arr[31]=1
        elif site=='Hadapsar':
                site_arr[32]=1
        elif site=='Hadapsar Industrial Estate':
                site_arr[33]=1
        elif site=='Hingne Khurd':
                site_arr[34]=1
        elif site=='Jangali Maharaj Road':
                site_arr[35]=1
        elif site=='Kalyani Nagar':
                site_arr[36]=1
        elif site=='Karve Nagar':
                site_arr[37]=1
        elif site=='Karve Road':
                site_arr[38]=1
        elif site=='Kasba Peth':
                site_arr[39]=1
        elif site=='Katraj':
                site_arr[40]=1
        elif site=='Khadaki':
                site_arr[41]=1
        elif site=='Khadki':
                site_arr[42]=1
        elif site=='Kharadi':
                site_arr[43]=1
        elif site=='Kondhwa':
                site_arr[44]=1
        elif site=='Kondhwa Budruk':
                site_arr[45]=1
        elif site=='Kondhwa Khurd':
                site_arr[46]=1
        elif site=='Koregaon Park':
                site_arr[47]=1
        elif site=='Kothrud':
                site_arr[48]=1
        elif site=='Law College Road':
                site_arr[49]=1
        elif site=='Laxmi Road':
                site_arr[50]=1
        elif site=='Lulla Nagar':
                site_arr[51]=1
        elif site=='Mahatma Gandhi Road':
                site_arr[52]=1
        elif site=='Mangalwar peth':
                site_arr[53]=1
        elif site=='Manik Bagh':
                site_arr[54]=1
        elif site=='Market yard':
                site_arr[55]=1
        elif site=='Model colony':
                site_arr[56]=1
        elif site=='Mukund Nagar':
                site_arr[57]=1
        elif site=='Mundhawa':
                site_arr[58]=1
        elif site=='Nagar Road':
                site_arr[59]=1
        elif site=='Nana Peth':
                site_arr[60]=1
        elif site=='Narayan Peth':
                site_arr[61]=1
        elif site=='Narayangaon':
                site_arr[62]=1
        elif site=='Navi Peth':
                site_arr[63]=1
        elif site=='Padmavati':
                site_arr[64]=1
        elif site=='Parvati Darshan':
                site_arr[65]=1
        elif site=='Pashan':
                site_arr[66]=1
        elif site=='Paud Road':
                site_arr[67]=1
        elif site=='Pirangut':
                site_arr[68]=1
        elif site=='Prabhat Road':
                site_arr[69]=1
        elif site=='Pune Railway Station':
                site_arr[70]=1
        elif site=='Rasta Peth':
                site_arr[71]=1
        elif site=='Raviwar Peth':
                site_arr[72]=1
        elif site=='Sadashiv Peth':
                site_arr[73]=1
        elif site=='Sahakar Nagar':
                site_arr[74]=1
        elif site=='Salunke Vihar':
                site_arr[75]=1
        elif site=='Sasson Road':
                site_arr[76]=1
        elif site=='Satara Road':
                site_arr[77]=1
        elif site=='Senapati Bapat Road':
                site_arr[78]=1
        elif site=='Shaniwar Peth':
                site_arr[79]=1
        elif site=='Shivaji Nagar':
                site_arr[80]=1
        elif site=='Shukrawar Peth':
                site_arr[81]=1
        elif site=='Sinhagad Road':
                site_arr[82]=1
        elif site=='Somwar Peth':
                site_arr[83]=1
        elif site=='Swargate':
                site_arr[84]=1
        elif site=='Tilak Road':
                site_arr[85]=1
        elif site=='Uruli Devachi':
                site_arr[86]=1
        elif site=='Vadgaon Budruk':
                site_arr[87]=1
        elif site=='Viman Nagar':
                site_arr[88]=1
        elif site=='Vishrant Wadi':
                site_arr[89]=1
        elif site=='Wadgaon Sheri':
                site_arr[90]=1
        elif site=='Wagholi':
                site_arr[91]=1
        elif site=='Wakadewadi':
                site_arr[92]=1
        elif site=='Wanowrie':
                site_arr[93]=1
        elif site=='Warje':
                site_arr[94]=1
        elif site=='Yerawada':
                site_arr[95]=1


        area = np.array([float(request.form["Land Area"])])
        bed = np.array([int(request.form["Bedrooms"])])
        bath = np.array([int(request.form["Bathrooms"])])
        bal = np.array([int(request.form["Balcony"])])

        x_arr = np.zeros(4)
        x_arr[0] = area
        x_arr[1] = bath
        x_arr[2] = bal
        x_arr[3] = bed

        x = np.concatenate([x_arr,site_arr])

        prediction=float(model.predict([x])[0])

    #.py -> HTML    
    return render_template('predict.html', a = area, s = site, b1 = bed, b2 = bath, b3 = bal, predicted_value = prediction)

if __name__=="__main__":
    app.run(debug=True)