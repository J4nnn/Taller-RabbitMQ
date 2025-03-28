package com.software3.producer.services;

import com.software3.producer.models.Message;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MessageService {

    private static final String EXCHANGE_NAME = "message.exchange";
    private static final String ROUTING_KEY = "message.key";

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public void sendMessage(Message message) {
        System.out.println("Message have been sent: " + message);
        rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY, message);
    }

}
