
from flask import Flask ,jsonify,request
from data import data

app=Flask(__name__)

@app.route("/getvalue")
def index():
    return jsonify({
        "datavalue":data,
        "message":"success"
    }),200


@app.route("/planet")
def planetname():
    #taking planet name from user
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "datavalue":planet_data,
        "message":"success"
    }),200
    
if __name__ == "__main__":
    app.run()