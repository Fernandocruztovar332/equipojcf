document.querySelector('input[value="Registrate"]').addEventListener('click', async () => {
    const nombre = document.querySelector('input[placeholder="Ingresa Tu Nombre(s)"]').value;
    const apellidos = document.querySelector('input[placeholder="Ingresa Tus Apellidos"]').value;
    const telefono = document.querySelector('input[placeholder="Ingresa Tu Telefono "]').value;
    const contraseña = document.querySelector('input[placeholder="Ingresa Una Contraseña"]').value;

    if (!nombre || !apellidos || !telefono || !contraseña) {
        alert('Todos los campos son obligatorios.');
        return;
    }

    try {
        const response = await fetch('http://localhost:3000/registrar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nombre, apellidos, telefono, contraseña }),
        });

        const data = await response.json();
        if (data.error) {
            alert('Error: ' + data.error);
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error('Error en la solicitud:', error);
        alert('No se pudo registrar el usuario.');
    }
});
