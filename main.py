from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route("/childa")
def childa():
    return render_template("child-A.html")

@app.route("/childb")
def childb():
    return render_template("child-B.html")

@app.route("/")
def parent():
    return render_template("child-A.html")

if __name__ == "__main__":
    app.run(debug=True)