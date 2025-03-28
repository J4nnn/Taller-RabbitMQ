package com.software3.producer.controllers;

import com.software3.producer.models.Message;
import com.software3.producer.services.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class MessageController {

    @Autowired
    private MessageService messageService;

    @GetMapping("/formulario")
    public String mostrarFormulario(Model model) {
        model.addAttribute("dato", new Message());
        return "formulario";
    }

    @PostMapping("/procesarFormulario")
    public String procesarFormulario(@RequestParam("datoInput") String message, Model model) {

        System.out.println("Dato recibido: " + message);

        model.addAttribute("datoRecibido", message);

        Message message1 = new Message();
        message1.setProducer("Java Producer");
        message1.setMessage(message);

        messageService.sendMessage(message1);
        return "formulario";
    }


}
