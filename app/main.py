from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))
    else:
        return "getted"