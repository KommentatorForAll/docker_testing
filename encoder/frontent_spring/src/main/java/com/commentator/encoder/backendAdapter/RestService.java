package com.commentator.encoder.backendAdapter;

import com.commentator.encoder.domain.Message;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

@Service
public class RestService {

    private final ObjectMapper objectMapper = new ObjectMapper();

    private final String baseUrl = "http://localhost:8000";

    private final RestTemplate restTemplate;

    public RestService(RestTemplateBuilder builder) {
        this.restTemplate = builder.build();
    }

    public Iterable<String> getAllEncoderTypes() {
        String url = baseUrl + "/encoders/list";
        String json = restTemplate.getForObject(url, String.class);
        try {
            return objectMapper.readValue(json, Iterable.class);
        }
        catch (Exception e) {
            System.err.println(e.getMessage());
            e.printStackTrace();
            return null;
        }
    }

    public List<Message> encode(Message message) {
        String url = baseUrl + String.format("/encoders/encode_url/%s/%s", URLEncoder.encode(message.type, StandardCharsets.UTF_8), URLEncoder.encode(message.message, StandardCharsets.UTF_8));
        Map<String, String> body = (Map<String, String>) restTemplate.postForObject(url, null, Map.class).get("messages");
        return body.entrySet().stream().map(e -> new Message(e.getKey(), e.getValue())).toList();
    }
}
