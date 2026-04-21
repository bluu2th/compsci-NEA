from flask import Flask, jsonify, render_template, url_for, request
import sqlite3
import json

app = Flask(__name__)

# List of resources
resources = [
    {
        "name": "NHS Mental Health",
        "url": "https://www.nhs.uk/mental-health/",
        "tags": [""]
    },
    {
        "name": "Mind UK",
        "url": "https://www.mind.org.uk/",
        "tags": [""]    
    },
    {
        "name": "Mind UK - Anxiety",
        "url": "https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety/",
        "tags": ["anxiety", "worry", "panic"]
    },
    {
        "name": "YoungMinds - Depression",
        "url": "https://www.youngminds.org.uk/young-person/mental-health-conditions/depression/",
        "tags": ["depression", "low mood", "sad"]
    },
    {
        "name": "Samaritans",
        "url": "https://www.samaritans.org/",
        "tags": ["crisis", "suicidal", "urgent", "harm"]
    },
    {
        "name": "",
        "url": "",
        "tags": ["a"]
    },
    {
        "name": "",
        "url": "",
        "tags": ["a"]
    },
    {
        "name": "",
        "url": "",
        "tags": ["a"]
    },
    {
        "name": "",
        "url": "",
        "tags": ["a"]
    },
    {
        "name": "",
        "url": "",
        "tags": ["a"]
    }
]
    


# Processing all together
def process_message(user_message, resources_list):
    category = classify_message(user_message)
    reply_text = generate_reply(category)
    matched = get_resources(category, resources_list)

    return reply_text, matched

# Home page
@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.post("/chat/")
def chat():
    user_msg = request.json["message"]
    reply, matched = process_message(user_msg, resources)
    return {"reply": reply, "resources": resources}

# A page listing all mental health resources from the website (mainly for primary stakeholders)
@app.route("/resources/")
def resources_list():
    return render_template("resources.html", resources = resources)

# A page listing all mental health resources for people to help out others (secondary stakeholders)
@app.route("/helping_out_others/")
def help_resources():
    help_resources = [
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
        {"name": "", "url": ""},
    ]
    return render_template("help_resources.html", help_resources = help_resources)

@app.route("/contact_us/")
def contact_us():
    return render_template("contact_us.html")


# Algorithm to determine which resources to give
# Classify the message to give resources
def classify_message(user_message):
    user_message = user_message.lower()

    crisis_keywords = ["suicide", "kill myself", "end it", "harm", "can't cope"]
    anxiety_keywords = ["anxiety", "panic", "worried", "overthinking"]
    depression_keywords = ["depressed", "sad", "empty", "low", "numb"]

    # Check for crisis first (highest priority)
    for word in crisis_keywords:
        if word in user_message:
            return "crisis"

    # Check for anxiety
    for word in anxiety_keywords:
        if word in user_message:
            return "anxiety"

    # Check for depression
    for word in depression_keywords:
        if word in user_message:
            return "depression"

    # If none found
    return "general"

def get_resources(category, resources):
    matched_resources = []

    for item in resources:
        if category in item["tags"]:
            matched_resources.append(item)

    return matched_resources

# Generate a supportive response
def generate_reply(category):
    if category == "crisis":
        return (
            "I'm really glad you reached out. It sounds like you're going through "
            "something overwhelming. You're not alone, and support is available."
        )

    if category == "anxiety":
        return (
            "It sounds like you're feeling anxious. That can be really tough, "
            "but there are ways to manage it and people who can help."
        )

    if category == "depression":
        return (
            "Feeling low or empty can be exhausting. You deserve support, "
            "and there are resources that might help you through this."
        )

    return (
        "Thank you for sharing how you're feeling. Here are some resources "
        "that might be helpful."
    )

@app.route("/test/")
def test():
    return render_template("test.html")



