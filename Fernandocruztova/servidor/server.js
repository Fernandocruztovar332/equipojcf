const express = require('express');
const bodyParser = require('body-parser');
const sql = require('mssql');

// Configuración de la base de datos SQL Server
const dbConfig = {
    user: 'tu_usuario',
    password: 'tu_contraseña',
    server: 'localhost', // Cambia por tu servidor SQL Server
    database: 'nombre_de_tu_base',
    options: {
        encrypt: true, // Para Azure
        trustServerCertificate: true, // Para conexiones locales
    },
};

const app = express();
app.use(bodyParser.json());

// Endpoint para ejecutar una consulta
app.post('/consulta', async (req, res) => {
    const { query } = req.body; // Recibe la consulta desde el cliente
    try {
        const pool = await sql.connect(dbConfig);
        const result = await pool.request().query(query);
        res.json(result.recordset); // Devuelve los resultados
    } catch (error) {
        res.status(500).send('Error ejecutando la consulta: ' + error.message);
    } finally {
        sql.close();
    }
});

// Iniciar el servidor
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
