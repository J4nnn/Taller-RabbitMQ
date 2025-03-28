const amqp = require('amqplib');
const express = require('express');

const app = express();
app.use(express.static('public'));

const rabbitSettings = {
    protocol: 'amqp',
    hostname: process.env.RABBITMQ_HOST,
    port: process.env.RABBITMQ_PORT,
    username: process.env.RABBITMQ_USER,
    password: process.env.RABBITMQ_PASSWORD,
    vhost: '/',
    authMechanism: ['PLAIN', 'AMQPLAIN', 'EXTERNAL']
}

let messages = [];

async function consumeMessages() {
    const queue = 'messages';
    const exchange = 'miFanoutExchange';

    const connection = await amqp.connect(rabbitSettings);
    const channel = await connection.createChannel();

    await channel.assertExchange(exchange, 'fanout', { durable: true });
    const q = await channel.assertQueue(queue, {durable: false});

    await channel.bindQueue(q.queue, exchange, '');

    channel.consume(queue, msg => {
        if (msg) {
            const receivedMessage = JSON.parse(msg.content.toString());
            messages.push(receivedMessage);
            channel.ack(msg);
        }
    })
}
consumeMessages();

app.get('/messages', (req, res) => {
    res.json(messages);
})

app.listen(3001, () => console.log('Consumer running on port 3001'));
