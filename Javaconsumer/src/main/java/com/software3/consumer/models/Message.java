package com.software3.consumer.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;

@Getter
@Setter
@AllArgsConstructor
public class Message implements Serializable {

    private String producer;
    private String message;

    @Override
    public String toString() {
        return getProducer() + ": " + getMessage();
    }

}
