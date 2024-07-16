from flask import Flask, render_template, request, jsonify, send_file
import openpyxl
import os

app = Flask(__name__)
DATABASE = 'data.xlsx'

# Inicializa el archivo Excel
def init_excel():
    if not os.path.exists(DATABASE):
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
        wb.save(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    wb = openpyxl.load_workbook(DATABASE)
    ws = wb.active
    row = [
        ','.join(data.get('nombre_residente', [])),
        ','.join(data.get('telefono_residente', [])),
        ','.join(data.get('celular_residente', [])),
        ','.join(data.get('cedula_residente', [])),
        ','.join(data.get('tipo_residente', [])),
        ','.join(data.get('nombre_inmobiliaria', [])),
        ','.join(data.get('telefono_inmobiliaria', [])),
        ','.join(data.get('nombre_propietario', [])),
        ','.join(data.get('direccion_propietario', [])),
        ','.join(data.get('telefono_propietario', [])),
        ','.join(data.get('ciudad_propietario', [])),
        ','.join(data.get('email_propietario', [])),
        ','.join(data.get('cedula_propietario', [])),
        ','.join(data.get('celular_propietario', [])),
        ','.join(data.get('nombre_residente_actual', [])),
        ','.join(data.get('identificacion_residente_actual', [])),
        ','.join(data.get('profesion_residente_actual', [])),
        ','.join(data.get('rh_residente_actual', [])),
        ','.join(data.get('edad_residente_actual', [])),
        ','.join(data.get('nombre_autorizado', [])),
        ','.join(data.get('identificacion_autorizado', [])),
        ','.join(data.get('parentesco_autorizado', [])),
        ','.join(data.get('marca_vehiculo', [])),
        ','.join(data.get('placa_vehiculo', [])),
        ','.join(data.get('parqueadero_vehiculo', [])),
        ','.join(data.get('conductor_vehiculo', [])),
        ','.join(data.get('color_vehiculo', [])),
        ','.join(data.get('modelo_vehiculo', [])),
        ','.join(data.get('mascotas', [])),
        ','.join(data.get('raza_mascota', [])),
        ','.join(data.get('numero_garaje', [])),
        ','.join(data.get('tiene_bicicleta', [])),
        ','.join(data.get('marca_bicicleta', [])),
        ','.join(data.get('color_bicicleta', [])),
        ','.join(data.get('nombre_emergencia', [])),
        ','.join(data.get('parentesco_emergencia', [])),
        ','.join(data.get('telefono_emergencia', []))
    ]
    ws.append(row)
    wb.save(DATABASE)
    return jsonify(success=True)

@app.route('/download', methods=['GET'])
def download():
    return send_file(DATABASE, as_attachment=True)

if __name__ == '__main__':
    init_excel()
    app.run(debug=True)
