document.getElementById('residenceForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        if (!data[key]) {
            data[key] = [];
        }
        data[key].push(value);
    });

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
      .then(data => {
          if(data.success) {
              alert('Formulario enviado exitosamente');
          } else {
              alert('Error al enviar el formulario');
          }
      });
});

function addResidente() {
    const container = document.getElementById('residentes_container');
    const newResidente = document.createElement('div');
    newResidente.className = 'residente';
    newResidente.innerHTML = `
        <label>Nombre:</label>
        <input type="text" name="nombre_residente_actual[]"><br>
        <label>Identificación:</label>
        <input type="text" name="identificacion_residente_actual[]"><br>
        <label>Profesión u oficio:</label>
        <input type="text" name="profesion_residente_actual[]"><br>
        <label>RH:</label>
        <input type="text" name="rh_residente_actual[]"><br>
        <label>Edad:</label>
        <input type="number" name="edad_residente_actual[]"><br>
    `;
    container.appendChild(newResidente);
}

function addAutorizado() {
    const container = document.getElementById('autorizados_container');
    const newAutorizado = document.createElement('div');
    newAutorizado.className = 'autorizado';
    newAutorizado.innerHTML = `
        <label>Nombre:</label>
        <input type="text" name="nombre_autorizado[]"><br>
        <label>Identificación:</label>
        <input type="text" name="identificacion_autorizado[]"><br>
        <label>Parentesco:</label>
        <input type="text" name="parentesco_autorizado[]"><br>
    `;
    container.appendChild(newAutorizado);
}

function addVehiculo() {
    const container = document.getElementById('vehiculos_container');
    const newVehiculo = document.createElement('div');
    newVehiculo.className = 'vehiculo';
    newVehiculo.innerHTML = `
        <label>Marca:</label>
        <input type="text" name="marca_vehiculo[]"><br>
        <label>Placa:</label>
        <input type="text" name="placa_vehiculo[]"><br>
        <label>Parqueadero Nº:</label>
        <input type="text" name="parqueadero_vehiculo[]"><br>
        <label>Nombre conductor:</label>
        <input type="text" name="conductor_vehiculo[]"><br>
        <label>Color:</label>
        <input type="text" name="color_vehiculo[]"><br>
        <label>Modelo:</label>
        <input type="text" name="modelo_vehiculo[]"><br>
    `;
    container.appendChild(newVehiculo);
}

function addEmergencia() {
    const container = document.getElementById('emergencia_container');
    const newEmergencia = document.createElement('div');
    newEmergencia.className = 'emergencia';
    newEmergencia.innerHTML = `
        <label>Nombre:</label>
        <input type="text" name="nombre_emergencia[]"><br>
        <label>Parentesco:</label>
        <input type="text" name="parentesco_emergencia[]"><br>
        <label>Teléfono(s):</label>
        <input type="tel" name="telefono_emergencia[]"><br>
    `;
    container.appendChild(newEmergencia);
}
