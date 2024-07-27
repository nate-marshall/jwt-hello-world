const express = require('express');
const path = require('path');
const axios = require('axios');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 8000;
const AUTH_SERVER_URL = process.env.AUTH_SERVER_URL || 'http://localhost:5000';

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, '../public')));

// Endpoint to handle login
app.post('/login', async (req, res) => {
    try {
        const response = await axios.post(`${AUTH_SERVER_URL}/login`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(error.response ? error.response.status : 500).json(error.response ? error.response.data : { message: 'Internal Server Error' });
    }
});

// Endpoint to handle protected resource
app.get('/protected', async (req, res) => {
    const token = req.headers['authorization'];
    try {
        const response = await axios.get(`${AUTH_SERVER_URL}/protected`, {
            headers: { 'Authorization': token }
        });
        res.json(response.data);
    } catch (error) {
        res.status(error.response ? error.response.status : 500).json(error.response ? error.response.data : { message: 'Internal Server Error' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
