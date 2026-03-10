from flask import Flask,jsonify,request,render_template,session
import random
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login")
def login():
    if request.method == "POST":
        mobile= request.form.get(mobile)
        password = request.form.get(password)
        print(mobile,password)
        otp = random.randint(100000,999999)
        session['otp'] = otp
        session['mobile'] = mobile
        print(f"otp for{mobile}is{otp}")
        return redirect("/verify")
    return render_template("login.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        username = request.form.get("Username")
        mobile = request.form.get("mobile")
        email=request.form.get("email")
        password = request.form.get("password")
        print(username,mobile,email,password)
        return "signup successful"
    return render_template("signup.html")
@app.route("/verify",methods=["GET","POST"])
def verify():
    
if __name__ == "__main__":
    app.run(debug=True)