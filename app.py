from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot_logic import get_emotional_response

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    mood_keywords = ["sad", "angry", "anxious", "empty", "confused"]

    if any(word in incoming_msg for word in mood_keywords):
        for word in mood_keywords:
            if word in incoming_msg:
                reply = get_emotional_response(word)
                break
    else:
        reply = "Hi, I’m EmotiBot 🌱 How are you feeling right now? (e.g., sad, anxious, angry)"

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
