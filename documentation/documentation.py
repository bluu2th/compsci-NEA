# File for getting screenshots for documentation
# Allows me to paste code chunks into here and have a clean workspace without the risk of breaking already created code



from flask import Flask, render_template
punctuation = ["!",'"',"'","£","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",";",":","@","<",">","/","?","#","~"]

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home_page.html")




crisis_keywords = ["suicide", "kill myself", "end it", "harm", "can't cope"] 
anxiety_keywords = ["anxiety", "stressed", "panic", "worried", "overthinking"] 
depression_keywords = ["depressed", "sad", "empty", "low", "numb"]


resources = [
    {
        "name": "NHS Mental Health",
        "url": "https://www.nhs.uk/mental-health/",
        "tags": ["general"]
    },
    {
        "name": "Mind UK",
        "url": "https://www.mind.org.uk/",
        "tags": ["general"]    
    },
    {
        "name": "Mind UK - Anxiety",
        "url": "https://www.mind.org.uk/anxiety",
        "tags": ["anxiety", "panic", "worry"]
    },
    {
        "name": "Mind UK",
        "url": "https://www.mind.org.uk/",
        "tags": ["anxiety", "panic", "worry"]
    }
]

# Normalisation of the user messages
def classify_message(user_message):
    user_message = user_message.lower()
    user_message = user_message.strip()
    for p in punctuation:
        user_message = user_message.replace(p, "")

# Keywords for classification
    crisis_keywords = ["suicide", "kill myself", "end it", "harm", "can't cope"]
    anxiety_keywords = ["anxiety", "panic", "worried", "overthinking"]
    depression_keywords = ["depressed", "sad", "empty", "low", "numb"]

# Returning the correct category based on keyword
    for word in crisis_keywords:
        if word in user_message:
            return "crisis"

    for word in anxiety_keywords:
        if word in user_message:
            return "anxiety"
    
    for word in depression_keywords:
        if word in user_message:
            return "depression"

    return "general"



def get_resources(category, resources):
    matched_resources = []

    for item in resources:
        if category in item["tags"]:
            matched_resources.append(item)

    return matched_resources


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

def process_message(user_message, resources_list):
    category = classify_message(user_message)
    reply_text = generate_reply(category)
    matched = get_resources(category, resources_list)

    return reply_text, matched
