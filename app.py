import numpy as np
import pickle
from flask import Flask, render_template,request

app=Flask(__name__)
model=pickle.load(open('insurancefraudmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    adriver=float(request.form['age_of_driver'])
    gender=float(request.form['gender'])
    mstatus=float(request.form['marital_status'])
    srating=float(request.form['safty_rating'])
    aincome=float(request.form['annual_income'])
    heducation=float(request.form['high_education_ind'])
    achange=float(request.form['address_change_ind'])
    lstatus=float(request.form['living_status'])
    cdate=float(request.form['claim_date'])
    asite=float(request.form['accident_site'])
    channel=float(request.form['channel'])
    preport=float(request.form['policy_report_filed_ind'])
    cpayout=float(request.form['claim_est_payout'])
    avehicle=float(request.form['age_of_vehicle'])
    vcategory=float(request.form['vehicle_category'])
    vprice=float(request.form['vehicle_price'])
    vcolor=float(request.form['vehicle_color'])
    vweight=float(request.form['vehicle_weight'])
    

    features = ([adriver,gender,mstatus,srating,aincome,heducation,achange,lstatus,cdate,asite,channel,preport,cpayout,avehicle,vcategory,vprice,vcolor,vweight])
    prediction=model.predict([features])
    if prediction == 1:
        result = "Is not fraud."
    else:
        result = "Is a fraud."
    return render_template('Result.html', predict= result)
    
    
    







if __name__=="__main__":
    app.run(debug=True)