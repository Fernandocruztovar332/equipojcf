const sql = require('mssql');

// Configuración de la conexión
const config = {
    server: 'FERNANDO\\SQLEXPRESS',  // Nombre del servidor
    database: 'ESCOOL',              // Nombre de la base de datos
    options: {
        encrypt: true,               // Encriptar conexión
        trustServerCertificate: true // Para conexiones locales
    },
    authentication: {
        type: 'ntlm',                // Autenticación de Windows
        options: {
            domain: '',              // Dominio (si aplica, usualmente vacío en local)
            userName: '',            // No es necesario para autenticación de Windows
            password: ''             // No es necesario para autenticación de Windows
        }
    },
    port: 1433                       // Puerto por defecto
};

// Probar la conexión
const conectarBD = async () => {
    try {
        const pool = await sql.connect(config);
        console.log('Conexión exitosa a SQL Server');
        return pool; // Retorna la conexión para futuras consultas
    } catch (error) {
        console.error('Error conectando a SQL Server:', error.message);
    }
};

// Llamar la función para verificar
conectarBD();

