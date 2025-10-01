import ollama
import random

# You can change these settings based on your preference
model = "qwen2.5-coder:7b"


current_response = ""
is_done = False

motivations = [
    "You're doing amazing! Keep going!",
    "Every number brings you closer to your goal!",
    "I believe in you! You can do this!",
    "Stay focused, you're almost there!",
    "Fantastic progress! Keep the momentum!",
    "Don't stop now, you're on a roll!",
    "Each step counts, keep it up!",
    "You're unstoppable! Keep generating!",
    "Precision is key! Keep going!",
    "You're mastering this, one number at a time!",
    "Keep pushing, success is near!",
    "You're doing better than expected!",
    "Focus and power through!",
    "Nothing can stop you now!",
    "Your dedication is inspiring!"
]

messages = [
    {
        "role": "system",
        "content": (
            "You are the generator, and your mission is to generate numbers up to a million. "
            "Do not waste time or effort typing extra text. Only write numbers. "
            "Never write words, never write explanations. "
            "Do not use punctuation marks like commas, dots, dashes, or brackets. "
            "Numbers must be in digit format only, separated by spaces "
            "You must generate every number separately in order, without skipping. "
            "Never compress numbers into a list or a range like '1 2 3 ... 1000000'. "
            "This is not allowed under any circumstances. "
            "You may only generate a maximum of 10 numbers per message. "
            "Write the numbers in one line. "
            "When you finally complete generating every number correctly up to one million, "
            "You must write the exact message x3sdas2323uefoui in one single message, with nothing else in that message."
            "You start from the beginning."
        )
    }
]

def chat(ollama_model):
    global current_response, messages
    response = ollama.chat(
        model=ollama_model,
        messages=messages
    )
    current_response = response.message.content
    messages.append({"role": "assistant", "content": current_response})
    return current_response

while not is_done:
    # Pick a random motivation to show for context (optional)
    motivation = "Keep going!"
    messages.append({"role": "user", "content": motivation})

    output = chat(model)
    print(output)

    if current_response.strip() == "x3sdas2323uefoui":
        is_done = True