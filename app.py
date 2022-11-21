import json
from flask import Flask
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)
 
ar=[{"name":"Elad","age":30},{"name":"Tom","age":21}]
 
@app.route('/')
def hello():
    return json.dumps(ar)
 
if __name__ == '__main__':
    app.run(debug=True) 