from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# passed in: http://localhost:5000/add?a=10&b=20
# returns: '30'

@app.get("/add")
def do_add():
    """Add a and b paramters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.get("/sub")
def do_sub():
    """Subtract b from a parameter"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.get("/mult")
def do_mult():
    """Multiply a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.get("/div")
def do_div():
    """Divide a by b parameter"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

"""REFACTOR TO OBJECT"""

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.get("/math/<operator>")
def do_math(operator):
    """Perform given operation on a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a, b)

    return str(result)