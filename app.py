from flask import Flask
from operations import Operations
app = Flask(__name__)

# passed in: http://localhost:5000/add?a=10&b=20
# returns: '30'

@app.get('/<operation>')
def perform_operation():

    a = request.args.get("a")
    b = request.args.get("b")

    Operations.{operation} =