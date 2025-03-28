package com.software3.consumer.config;

import org.springframework.amqp.core.*;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.amqp.support.converter.MessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    @Bean
    public Queue queue() {
        return new Queue("message.queue", true);
    }

    @Bean
    public DirectExchange exchange() {
        return new DirectExchange("message.exchange");
    }

    @Bean
    public FanoutExchange fanoutExchange() {
        return new FanoutExchange("miFanoutExchange");
    }

    @Bean
    public Binding bindingFanout(FanoutExchange fanoutExchange, Queue queue) {
        return BindingBuilder.bind(queue).to(fanoutExchange);
    }

    @Bean
    public Binding bindingDirect(Queue queue, DirectExchange exchange) {
        return BindingBuilder.bind(queue).to(exchange).with("message.key");
    }

    @Bean
    public MessageConverter jsonMessageConverter() {
        return new Jackson2JsonMessageConverter();
    }

    @Bean
    public RabbitTemplate rabbitTemplate(ConnectionFactory connectionFactory) {
        RabbitTemplate rabbitTemplate = new RabbitTemplate(connectionFactory);
        rabbitTemplate.setMessageConverter(jsonMessageConverter()); // Configura JSON como formato
        return rabbitTemplate;
    }

}
