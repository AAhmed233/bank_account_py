from flask import Flask,request,render_template,jsonify,redirect,url_for,session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/home")
def Home():
    return render_template("parent.html")

@app.route("/create-account")
def createAccount():
    return render_template("createAccount.html")

@app.route("/childb")
def childb():
    return render_template("child-B.html")

@app.route("/")
def parent():
    return render_template("parent.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["ref"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))  


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        session.permanent = True
        # Récupérer les trois champs
        user_ref = request.form["ref"]
        user_name = request.form["name"]
        user_price = request.form["price"]
        # Enregistrer dans la session
        session["ref"] = user_ref
        session["name"] = user_name
        session["price"] = user_price
        
        return redirect(url_for("aff"))
    else:
        if "ref" in session and "name" in session and "price" in session:
            return redirect(url_for("aff"))
        return render_template("login.html")


@app.route("/aff")
def aff():
    if "ref" in session and "name" in session and "price" in session:
        user_ref = session["ref"]
        user_name = session["name"]
        user_price = session["price"]
        # Afficher les trois propriétés
        return f"""
        <h1>Informations utilisateur :</h1>
        <p><strong>Ref:</strong> {user_ref}</p>
        <p><strong>Nom:</strong> {user_name}</p>
        <p><strong>Prix:</strong> {user_price}</p>
        """
    else:
        return redirect(url_for("add"))


if __name__ == "__main__":
    app.run(debug=True)