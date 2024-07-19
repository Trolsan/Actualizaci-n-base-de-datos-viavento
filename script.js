document.getElementById('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);
    const jsonData = {};
    data.forEach((value, key) => jsonData[key] = value);
    try {
        const response = await fetch('mongodb://mongo:WCPqrmtCDXLNtIyeMdauXSnyrseRhHlK@monorail.proxy.rlwy.net:57154/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error:', error);
        alert('Error al enviar los datos');
    }
});

//document.getElementById('download-btn').addEventListener('click', function() {
//    fetch('/download')
//        .then(response => response.blob())
//        .then(blob => {
//            const url = window.URL.createObjectURL(blob);
//            const a = document.createElement('a');
//            a.style.display = 'none';
//            a.href = url;
//            a.download = 'residents.xlsx';
//            document.body.appendChild(a);
//            a.click();
//            window.URL.revokeObjectURL(url);
//        })
//        .catch(error => console.error('Error:', error));
//});



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
