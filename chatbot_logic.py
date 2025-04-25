def get_emotional_response(mood):
    if mood == "sad":
        return "I'm here for you. Would you like to try a 1-minute breathing exercise?"
    elif mood == "anxious":
        return "Let's take a deep breath together. Inhale... Exhale... Feeling any better?"
    elif mood == "angry":
        return "It’s okay to feel that way. Want to write down what triggered it?"
    elif mood == "empty":
        return "Even feeling numb is valid. Want a positive affirmation?"
    else:
        return "I'm always here to listen. What’s on your mind?"
