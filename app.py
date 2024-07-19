import os
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS # type: ignore
from pymongo import MongoClient # type: ignore
import openpyxl

app = Flask(__name__)
CORS(app)  # Habilita CORS en toda la aplicación

# Configura la conexión a la base de datos MongoDB
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongo:WCPqrmtCDXLNtIyeMdauXSnyrseRhHlK@mongodb.railway.internal:27017')
client = MongoClient(MONGO_URI)
db = client.get_database()

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir los datos del formulario
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    db.residents.insert_one(data)
    response = {'status': 'success', 'message': 'Datos recibidos correctamente'}
    return jsonify(response)



# Ruta para descargar los datos en un archivo Excel
@app.route('/download', methods=['GET'])
def download():
    residents = db.residents.find()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Nombre Residente', 'Teléfono Residente', 'Celular Residente', 'Cédula Residente', 'Tipo Residente', 
               'Nombre Inmobiliaria', 'Teléfono Inmobiliaria', 'Nombre Propietario', 'Dirección Propietario',
               'Teléfono Propietario', 'Ciudad Propietario', 'Email Propietario', 'Cédula Propietario', 'Celular Propietario',
               'Nombre Residente Actual', 'Identificación Residente Actual', 'Profesión Residente Actual', 'RH Residente Actual',
               'Edad Residente Actual', 'Nombre Autorizado', 'Identificación Autorizado', 'Parentesco Autorizado', 'Marca Vehículo',
               'Placa Vehículo', 'Parqueadero Vehículo', 'Conductor Vehículo', 'Color Vehículo', 'Modelo Vehículo', 'Mascotas',
               'Raza Mascota', 'Número Garaje', 'Tiene Bicicleta', 'Marca Bicicleta', 'Color Bicicleta', 'Nombre Emergencia',
               'Parentesco Emergencia', 'Teléfono Emergencia'])
    for resident in residents:
        ws.append([resident.get('nombre_residente'), resident.get('telefono_residente'), resident.get('celular_residente'), resident.get('cedula_residente'), resident.get('tipo_residente'), 
                   resident.get('nombre_inmobiliaria'), resident.get('telefono_inmobiliaria'), resident.get('nombre_propietario'), resident.get('direccion_propietario'),
                   resident.get('telefono_propietario'), resident.get('ciudad_propietario'), resident.get('email_propietario'), resident.get('cedula_propietario'), resident.get('celular_propietario'),
                   resident.get('nombre_residente_actual'), resident.get('identificacion_residente_actual'), resident.get('profesion_residente_actual'), resident.get('rh_residente_actual'),
                   resident.get('edad_residente_actual'), resident.get('nombre_autorizado'), resident.get('identificacion_autorizado'), resident.get('parentesco_autorizado'), resident.get('marca_vehiculo'),
                   resident.get('placa_vehiculo'), resident.get('parqueadero_vehiculo'), resident.get('conductor_vehiculo'), resident.get('color_vehiculo'), resident.get('modelo_vehiculo'), resident.get('mascotas'),
                   resident.get('raza_mascota'), resident.get('numero_garaje'), resident.get('tiene_bicicleta'), resident.get('marca_bicicleta'), resident.get('color_bicicleta'), resident.get('nombre_emergencia'),
                   resident.get('parentesco_emergencia'), resident.get('telefono_emergencia')])
    wb.save('residents.xlsx')
    return send_file('residents.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)