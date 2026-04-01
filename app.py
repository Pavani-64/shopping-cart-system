from flask import Flask, render_template, request, redirect, session
from database import (
    create_tables,
    add_user,
    check_user,
    add_to_cart,
    get_cart,
    remove_item,
    clear_cart
)

app = Flask(__name__)
app.secret_key = "secret123"

create_tables()


# ---------- HOME ----------
@app.route("/")
def home():
    return redirect("/login")


# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if check_user(user, pwd):
            session["user"] = user
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return render_template("login.html")


# ---------- SIGNUP ----------
@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if add_user(user, pwd):
            return redirect("/login")
        else:
            return "User already exists"

    return render_template("signup.html")


# ---------- DASHBOARD ----------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        qty = int(request.form["qty"])

        add_to_cart(username, name, price, qty)

    items = get_cart(username)

    return render_template("dashboard.html", items=items)


# ---------- REMOVE ITEM ----------
@app.route("/remove/<name>")
def remove(name):
    if "user" not in session:
        return redirect("/login")

    remove_item(session["user"], name)
    return redirect("/dashboard")


# ---------- CHECKOUT ----------
@app.route("/checkout")
def checkout():
    if "user" not in session:
        return redirect("/login")

    items = get_cart(session["user"])

    total = sum(item[1] * item[2] for item in items)

    clear_cart(session["user"])

    return f"""
    <div style='text-align:center; margin-top:50px; font-family:Arial'>
        <h2>✅ Order Placed Successfully!</h2>
        <h3>Total Paid: ₹{total}</h3>
        <a href='/dashboard'>⬅ Back to Dashboard</a>
    </div>
    """


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)