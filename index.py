from flask import Flask,jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["admin"]
collection = db["films"]
@app.route("/films/get/all",methods=["GET"])
def get_all_films():
    films = list(collection.find({}))
    return jsonify(films)
if __name__ == "__main__":
    app.run(debug=True)