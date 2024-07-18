from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import openpyxl
import os

app = Flask(__name__)
CORS(app, resources= {r"/*":{"origins": "https://basedatosviavento-production-38e8.up.railway.app"}})  # Habilita CORS en toda la aplicación

DATABASE = 'data.xlsx'

# Inicializa el archivo Excel
def init_excel():
    if not os.path.exists(DATABASE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append([
            'Nombre Residente', 'Teléfono Residente', 'Celular Residente', 'Cédula Residente', 'Tipo Residente', 
            'Nombre Inmobiliaria', 'Teléfono Inmobiliaria', 'Nombre Propietario', 'Dirección Propietario', 
            'Teléfono Propietario', 'Ciudad Propietario', 'Email Propietario', 'Cédula Propietario', 'Celular Propietario',
            'Nombre Residente Actual', 'Identificación Residente Actual', 'Profesión Residente Actual', 'RH Residente Actual', 
            'Edad Residente Actual', 'Nombre Autorizado', 'Identificación Autorizado', 'Parentesco Autorizado', 'Marca Vehículo', 
            'Placa Vehículo', 'Parqueadero Vehículo', 'Conductor Vehículo', 'Color Vehículo', 'Modelo Vehículo', 'Mascotas', 
            'Raza Mascota', 'Número Garaje', 'Tiene Bicicleta', 'Marca Bicicleta', 'Color Bicicleta', 'Nombre Emergencia', 
            'Parentesco Emergencia', 'Teléfono Emergencia'
        ])
        wb.save(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    wb = openpyxl.load_workbook(DATABASE)
    ws = wb.active
    row = [
        data.get('nombre_residente'),
        data.get('telefono_residente'),
        data.get('celular_residente'),
        data.get('cedula_residente'),
        data.get('tipo_residente'),
        data.get('nombre_inmobiliaria'),
        data.get('telefono_inmobiliaria'),
        data.get('nombre_propietario'),
        data.get('direccion_propietario'),
        data.get('telefono_propietario'),
        data.get('ciudad_propietario'),
        data.get('email_propietario'),
        data.get('cedula_propietario'),
        data.get('celular_propietario'),
        data.get('nombre_residente_actual'),
        data.get('identificacion_residente_actual'),
        data.get('profesion_residente_actual'),
        data.get('rh_residente_actual'),
        data.get('edad_residente_actual'),
        data.get('nombre_autorizado'),
        data.get('identificacion_autorizado'),
        data.get('parentesco_autorizado'),
        data.get('marca_vehiculo'),
        data.get('placa_vehiculo'),
        data.get('parqueadero_vehiculo'),
        data.get('conductor_vehiculo'),
        data.get('color_vehiculo'),
        data.get('modelo_vehiculo'),
        data.get('mascotas'),
        data.get('raza_mascota'),
        data.get('numero_garaje'),
        data.get('tiene_bicicleta'),
        data.get('marca_bicicleta'),
        data.get('color_bicicleta'),
        data.get('nombre_emergencia'),
        data.get('parentesco_emergencia'),
        data.get('telefono_emergencia')
    ]
    ws.append(row)
    wb.save(DATABASE)
    return jsonify(success=True)


@app.route('/download', methods=['GET'])
def download():
    file_path = 'datos.xlsx'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    init_excel()
    app.run(debug=True)
