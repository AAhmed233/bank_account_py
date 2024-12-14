from flask import Flask,request,render_template,jsonify # type: ignore
from services import Storage
from model import Product
app = Flask(__name__)

@app.route("/store")
def listProduct():
    return Storage.list()

@app.route("/store/search",methods=['GET','POST'])
def search():
    ref = request.form.get('ref')
    if ref != None:
        product:Product|None=Storage.search(ref)
        if Product != None:
            return jsonify(product)
    return "Not found"

@app.route("/store/add",methods=['POST'])
def add():
    body= request.get_json()
    product:Product=Product(**body)
    if Storage.add(product):
        return 'Add ok',201
    return 'No add',500

@app.route("/")
def index():
    return render_template("index.html")



#render_template("index.html")

# PAth Request
@app.route("/hello/<name>")
def say_hello(name:str):
    return f"<h1 style='color:red;text-align:center'>Hello {name}</h1>"

#render_template("index.html",p=name) 
#f"<h1 style='color:red;text-align:center'>Hello {name}</h1>"

@app.route("/profile")
def profile():
    programe_age = request.args.get("age",0)
    return f"<h1 style='color:red;text-align:center'>your age is {programe_age}</h1>"


if __name__ == "__main__":
    app.run(debug=True)