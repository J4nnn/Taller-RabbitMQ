const express = require('express');
const amqp = require('amqplib');

const app = express();
app.use(express.json());
app.use(express.static('public'));

const rabbitSettings = {
    protocol: 'amqp',
    hostname: 'rabbitmq',
    port: 5672,
    username: 'guest',
    password: 'guest',
    vhost: '/',
    authMechanism: ['PLAIN', 'AMQPLAIN', 'EXTERNAL']
}

async function sendMessage(message) {
    try {
        const queue = 'messages';
        const exchange = 'miFanoutExchange'
        const connection = await amqp.connect(rabbitSettings);
        const channel = await connection.createChannel();

        await channel.assertExchange(exchange, 'fanout', {durable: true})
        await channel.assertQueue(queue, { durable: false });

        channel.sendToQueue(queue, Buffer.from(JSON.stringify({producer: 'Node producer', message: message })));
        channel.publish(exchange, '', Buffer.from(JSON.stringify({producer: 'Node producer', message: message})));
        console.log(`Mensaje enviado: ${message}`);

        await channel.close();
        await connection.close();
    } catch (error) {
        console.error("Error al enviar mensaje:", error);
    }
}

// Ruta para recibir el mensaje desde el frontend
app.post('/send', async (req, res) => {
    try {
        const { text } = req.body;

        if (!text) {
            return res.status(400).send({ error: 'El campo "text" es obligatorio' });
        }

        await sendMessage(text);
        res.send({ status: 'Message sent' });
    } catch (error) {
        console.error("Error en /send:", error);
        res.status(500).send({ error: 'Error interno del servidor' });
    }
});

// Servidor Express
app.listen(3000, () => console.log('Producer running on port 3000'));
