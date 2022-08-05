package com.commentator.encoder.domain;


public class Message {
    public String getMessage() {
        return message;
    }

    public Message(String type, String message) {
        this.message = message;
        this.type = type;
    }

    public Message() {
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String message, type;

    public String toString() {
        return String.format("message '%s' of type '%s'", message, type);
    }
}
