from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get("/add")
def addition():
    a = request.args["a"]
    b = request.args["b"]

    return str(add(int(a), int(b)))

@app.get("/sub")
def subtraction():
    a = request.args["a"]
    b = request.args["b"]

    return str(sub(int(a), int(b)))

@app.get("/mult")
def multiply():
    a = request.args["a"]
    b = request.args["b"]

    return str(mult(int(a), int(b)))

@app.get("/div")
def divide():
    a = request.args["a"]
    b = request.args["b"]

    return str(div(int(a), int(b)))