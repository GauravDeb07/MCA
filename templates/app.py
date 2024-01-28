
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("try.html")
@app.route('/PatientLogin.html')
def PatientLogin():
    return render_template("PatientLogin.html")
@app.route('/DoctorLogin.html')
def DoctorLoginLogin():
    return render_template("DoctorLogin.html")
@app.route('/login',methods=["POST"])
def main():
    if request.method == "POST":
        try:
            log=request.form.get('loginUsername')
            return render_template("main.html",log=log)
        except Exception as e:
            return f"sn error:{e}"
@app.route('/login2',methods=["POST"])
def main2():
    if request.method == "POST":
        try:
            log=request.form.get('loginUsername')
            return render_template("main2.html",log=log)
        except Exception as e:
            return f"sn error:{e}"
@app.route('/SkinSymptom', methods=["POST"])
def detail():
    if request.method == "POST":
        try:
            age = request.form.get('Age')
            gender = request.form.get('Gender')
            weight = request.form.get('Weight')
            height = request.form.get('Height')
            blood_type = request.form.get('BloodType')
            
            return render_template("skin.html", age=age, gender=gender, weight=weight, height=height, blood_type=blood_type)
        except Exception as e:
            return f"An error occurred: {e}"

@app.route('/submit_doctor_details', methods=["POST"])
def detail2():
    if request.method == "POST":
        try:
            specialization = request.form.get('Specialization')
            hospital = request.form.get('hospital')
            experience = request.form.get('Experience')
            contact_number = request.form.get('contact_number')
            
            return render_template("drmain.html", specialization=specialization, hospital=hospital, experience=experience, contact_number=contact_number)
        except Exception as e:
            return f"An error occurred: {e}"

 
@app.route('/RespiratorySymptoms',methods=["POST"])
def skin():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("respiratory.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/JointMuscle',methods=["POST"])
def respiratory():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("JointandMuscle.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/Digestive',methods=["POST"])
def JointMuscle():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("digestive.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/Urinary',methods=["POST"])
def Digestive():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("Urinary.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"


@app.route('/NervousSystem',methods=["POST"])
def Urinary():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("NervousSystem.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/Cardiovascular',methods=["POST"])
def NervousSystem():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("Cardiovascular.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/MentalEmotional',methods=["POST"])
def Cardiovascular():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("MentalEmotional.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/other',methods=["POST"])
def MentalEmotional():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("Other.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"

@app.route('/Result',methods=["POST"])
def Other():
    if request.method == "POST":
        try:
            symptoms = request.form.getlist('symptoms[]')
            syn= ', '.join(symptoms)
            return render_template("Result.html", log=syn)
        except Exception as e:
            return f"sn error: {e}"


if __name__ == '__main__':
    app.run(debug=True)