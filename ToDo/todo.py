from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # For flash messages

# MongoDB connection
uri = "mongodb+srv://patelsnklp:asdfg@cluster0.6ltcang.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'), tlsAllowInvalidCertificates=True)

# Select database and collection
db = client["todo"]
collection = db["item_storage"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if item_name and item_description:
        collection.insert_one({
            "name": item_name,
            "description": item_description
        })
        flash("Item submitted successfully!")
    else:
        flash("Both fields are required.", "error")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

