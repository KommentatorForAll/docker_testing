package com.commentator.encoder.web;

import com.commentator.encoder.backendAdapter.RestService;
import com.commentator.encoder.domain.Message;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.awt.*;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

@Controller
public class PageController {

    public PageController(@Autowired RestService restService) {
        this.restService = restService;
        Random rnd = new Random();
        for (String type : restService.getAllEncoderTypes()) {
            colors.put(type, "#" +Integer.toHexString(rnd.nextInt(255*255*255)));
        }
    }

    RestService restService;

    Map<String, String> colors = new HashMap<>();

    @GetMapping({"/", "index", "index.html"})
    public String homepage(Model model) {
        Message message = (Message) model.getAttribute("message");
        if (message==null) {
            message = new Message("string", "Hello, World!");
        }
        List<Message> msgs = restService.encode(message);
        model.addAttribute("messages", msgs);
        model.addAttribute("message", message);
        model.addAttribute("colors", colors);
        return "index";
    }

    @PostMapping({"/", "index", "index.html"})
    public String encode(@ModelAttribute("message") Message message, Model model, RedirectAttributes attributes) {
        List<Message> msgs = restService.encode(message);
        model.addAttribute("messages", msgs);
        model.addAttribute("colors", colors);
        return "index";
    }
}
