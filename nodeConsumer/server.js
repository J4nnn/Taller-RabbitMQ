const amqp = require('amqplib');
const express = require('express');

const app = express();
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

const queue = 'messages';
let messages = [];

async function consumeMessages() {
    const connection = await amqp.connect(rabbitSettings);
    const channel = await connection.createChannel();
    await channel.assertExchange(queue);
    
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
