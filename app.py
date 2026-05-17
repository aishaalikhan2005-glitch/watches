from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "rolex_secret_key"

# Temporary storage (no database as per lab requirement)
users = {}

@app.route("/admin")
def admin():
    return users

# ---------------- HOME (Protected) ----------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])


# ---------------- ABOUT ----------------
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- SERVICES ----------------
@app.route("/services")
def services():
    return render_template("services.html")


# ---------------- GALLERY ----------------
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# ---------------- CONTACT ----------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        if not fullname or not email or not username or not password:
            return render_template("register.html", message="All fields are required!")

        elif username in users:
            return render_template("register.html", message="User already exists!")

        else:
            users[username] = {
                "fullname": fullname,
                "email": email,
                "password": password
            }

            return redirect(url_for("login"))   # 🔥 IMPORTANT

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    message = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            message = "Invalid username or password! Please register first."

    return render_template("login.html", message=message)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])