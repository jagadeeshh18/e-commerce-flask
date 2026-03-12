from flask import Flask, jsonify, request, render_template, session, redirect
import random
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey18"
def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mobile = request.form.get("mobile")
        password = request.form.get("password")
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("select * from users where mobile = ? and password = ?",(mobile,password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            otp = random.randint(100000, 999999)
            session['otp'] = otp
            session['mobile'] = mobile

            print(f"otp for {mobile} is {otp}")

            return redirect("/verify")
        else:
            return " user not found"
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        mobile = request.form.get("mobile")
        password = request.form.get("password")
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("insert into users(username,mobile,password) values(?,?,?)",(username,mobile,password))
        conn.commit()
        conn.close()

        print(username, mobile, password)

        return redirect("/login") 

    return render_template("signup.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        usr_otp = request.form.get("otp")
        real_otp = session.get('otp')

        if usr_otp and int(usr_otp) == real_otp:
            return "login successful"
        else:
            return "invalid otp"

    return render_template("verifyotp.html")


if __name__ == "__main__":
    app.run(debug=True)
