from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Configuración de la conexión a MongoDB
# Asegúrate de definir tu variable de entorno MONGO_URI en Railway
client = MongoClient(os.getenv('MONGO_URI'))
db = client['test']
collection = db['usuarios']

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Guardar los datos en MongoDB
    collection.insert_one(data)
    return jsonify({"message": "Datos guardados con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)