from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import openpyxl
import os

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:figWHPeRMbNkCjhPBgGhSmyfqYaOapOu@monorail.proxy.rlwy.net:30875/railway"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_residente = Column(String, nullable=False)
    telefono_residente = Column(String, nullable=False)
    celular_residente = Column(String, nullable=False)
    cedula_residente = Column(String, nullable=False)
    tipo_residente = Column(String, nullable=False)
    nombre_inmobiliaria = Column(String, nullable=False)
    telefono_inmobiliaria = Column(String, nullable=False)
    nombre_propietario = Column(String, nullable=False)
    direccion_propietario = Column(String, nullable=False)
    telefono_propietario = Column(String, nullable=False)
    ciudad_propietario = Column(String, nullable=False)
    email_propietario = Column(String, nullable=False)
    cedula_propietario = Column(String, nullable=False)
    celular_propietario = Column(String, nullable=False)
    nombre_residente_actual = Column(String, nullable=False)
    identificacion_residente_actual = Column(String, nullable=False)
    profesion_residente_actual = Column(String, nullable=False)
    rh_residente_actual = Column(String, nullable=False)
    edad_residente_actual = Column(String, nullable=False)
    nombre_autorizado = Column(String, nullable=False)
    identificacion_autorizado = Column(String, nullable=False)
    parentesco_autorizado = Column(String, nullable=False)
    marca_vehiculo = Column(String, nullable=False)
    placa_vehiculo = Column(String, nullable=False)
    parqueadero_vehiculo = Column(String, nullable=False)
    conductor_vehiculo = Column(String, nullable=False)
    color_vehiculo = Column(String, nullable=False)
    modelo_vehiculo = Column(String, nullable=False)
    mascotas = Column(String, nullable=False)
    raza_mascota = Column(String, nullable=False)
    numero_garaje = Column(String, nullable=False)
    tiene_bicicleta = Column(String, nullable=False)
    marca_bicicleta = Column(String, nullable=False)
    color_bicicleta = Column(String, nullable=False)
    nombre_emergencia = Column(String, nullable=False)
    parentesco_emergencia = Column(String, nullable=False)
    telefono_emergencia = Column(String, nullable=False)

Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('monorail.proxy.rlwy.net:30875/submit', methods=['POST'])
def submit():
    data = request.json
    new_user = User(
        nombre_residente=data['nombre_residente'],
        telefono_residente=data['telefono_residente'],
        celular_residente=data['celular_residente'],
        cedula_residente=data['cedula_residente'],
        tipo_residente=data['tipo_residente'],
        nombre_inmobiliaria=data['nombre_inmobiliaria'],
        telefono_inmobiliaria=data['telefono_inmobiliaria'],
        nombre_propietario=data['nombre_propietario'],
        direccion_propietario=data['direccion_propietario'],
        telefono_propietario=data['telefono_propietario'],
        ciudad_propietario=data['ciudad_propietario'],
        email_propietario=data['email_propietario'],
        cedula_propietario=data['cedula_propietario'],
        celular_propietario=data['celular_propietario'],
        nombre_residente_actual=data['nombre_residente_actual'],
        identificacion_residente_actual=data['identificacion_residente_actual'],
        profesion_residente_actual=data['profesion_residente_actual'],
        rh_residente_actual=data['rh_residente_actual'],
        edad_residente_actual=data['edad_residente_actual'],
        nombre_autorizado=data['nombre_autorizado'],
        identificacion_autorizado=data['identificacion_autorizado'],
        parentesco_autorizado=data['parentesco_autorizado'],
        marca_vehiculo=data['marca_vehiculo'],
        placa_vehiculo=data['placa_vehiculo'],
        parqueadero_vehiculo=data['parqueadero_vehiculo'],
        conductor_vehiculo=data['conductor_vehiculo'],
        color_vehiculo=data['color_vehiculo'],
        modelo_vehiculo=data['modelo_vehiculo'],
        mascotas=data['mascotas'],
        raza_mascota=data['raza_mascota'],
        numero_garaje=data['numero_garaje'],
        tiene_bicicleta=data['tiene_bicicleta'],
        marca_bicicleta=data['marca_bicicleta'],
        color_bicicleta=data['color_bicicleta'],
        nombre_emergencia=data['nombre_emergencia'],
        parentesco_emergencia=data['parentesco_emergencia'],
        telefono_emergencia=data['telefono_emergencia']
    )
    session.add(new_user)
    session.commit()
    return jsonify({"message": "Data saved successfully"}), 200



@app.route('monorail.proxy.rlwy.net:30875/download', methods=['GET'])
def download():
    users = session.query(User).all()

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

    for user in users:
        ws.append([
            user.nombre_residente, user.telefono_residente, user.celular_residente, user.cedula_residente, user.tipo_residente,
            user.nombre_inmobiliaria, user.telefono_inmobiliaria, user.nombre_propietario, user.direccion_propietario,
            user.telefono_propietario, user.ciudad_propietario, user.email_propietario, user.cedula_propietario, user.celular_propietario,
            user.nombre_residente_actual, user.identificacion_residente_actual, user.profesion_residente_actual, user.rh_residente_actual,
            user.edad_residente_actual, user.nombre_autorizado, user.identificacion_autorizado, user.parentesco_autorizado, user.marca_vehiculo,
            user.placa_vehiculo, user.parqueadero_vehiculo, user.conductor_vehiculo, user.color_vehiculo, user.modelo_vehiculo, user.mascotas,
            user.raza_mascota, user.numero_garaje, user.tiene_bicicleta, user.marca_bicicleta, user.color_bicicleta, user.nombre_emergencia,
            user.parentesco_emergencia, user.telefono_emergencia
        ])

    file_path = 'users_data.xlsx'
    wb.save(file_path)

    return send_file(file_path, as_attachment=True)

