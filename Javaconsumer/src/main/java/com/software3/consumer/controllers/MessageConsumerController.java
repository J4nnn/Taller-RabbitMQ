package com.software3.consumer.controllers;

import com.software3.consumer.models.Message;
import com.software3.consumer.services.MessageConsumerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class MessageConsumerController {

    @Autowired
    private MessageConsumerService messageService;

    @GetMapping("/messages")
    public String getMessage(Model model) {
        model.addAllAttributes(messageService.getMessages());
        return "index";
    }

}
