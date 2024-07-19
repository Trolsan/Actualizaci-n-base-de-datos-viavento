from flask import Flask, request, redirect, url_for, render_template
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
CORS(app)

# Configuración de la conexión a MongoDB
client = MongoClient(os.getenv('mongodb://mongo:WCPqrmtCDXLNtIyeMdauXSnyrseRhHlK@mongodb.railway.internal:27017'))
db = client['test']
collection = db['usuarios']

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    collection.insert_one(data)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "Datos guardados con éxito"

if __name__ == '__main__':
    app.run(debug=True)