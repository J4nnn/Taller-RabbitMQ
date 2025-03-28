package com.software3.consumer.services;

import com.software3.consumer.models.Message;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class MessageConsumerService {

    private final List<Message> messages;

    public MessageConsumerService(List<Message> messages) {
        this.messages = messages;
    }

    @RabbitListener(queues = "message.queue")
    public void receiveMessage(Message message) {
        System.out.println("Received message: " + message);
        this.messages.add(message);
    }

    public Map<String, List<Message>> getMessages() {
        Map<String, List<Message>> map = new HashMap<>();
        map.put("messages", messages);
        return map;
    }

}
