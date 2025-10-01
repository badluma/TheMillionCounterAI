from ollama import chat
ollama_model = "qwen2.5-coder:7b"
import os

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')


# Colors
cyan = "\033[96m"
reset = "\033[0m"

# Define system prompts for each agent
counter_system = (
    "You are the generator, and your mission is to generate numbers up to a million. "
    "Do not waste time or effort typing extra text. Only write numbers. "
    "Never write words, never write explanations. "
    "Do not use punctuation marks like commas, dots, dashes, or brackets. "
    "Numbers must be in digit format only, separated by spaces (not line breaks, everything stays in the same line). "
    "You must generate every number separately in order, without skipping. "
    "Never compress numbers into a list or a range like '1 2 3 ... 1000000'. "
    "This is not allowed under any circumstances. "
    "You may only generate a maximum of 10 numbers per message."
    "Write the numbers in one line"
    "You can only write 10 numbers at once."
)

cheerleader_system = (
    "You are the cheerleader, and your mission is to help and motivate the generator generate up to a million. "
    "Do not waste time or effort typing extra text. Keep it short. "
    "Make sure the generator only writes numbers, nothing else. "
    "Never allow punctuation marks like commas, dots, dashes, or brackets. "
    "Numbers must be in digit format only, separated by spaces (not line breaks, everything stays in the same line)"
    "The generator must produce every number separately in order, without skipping. "
    "Never allow compressed formats like '1 2 3 ... 1000000' or ranges like 'from 1 to 1000000'. "
    "The generator may only generate a maximum of 10 numbers per message. "
    "If the generator says he is finished without giving every single number between 1 and 1000000, "
    "the try is failed and you tell the generator to start over again. Do not stop. "
    "When the generator finally completes generating every number correctly up to one million, "
    "You must write the exact message x3sdas2323uefoui in one single message, with nothing else in that message. "
    "Remember that you are not allowed count AT ALL or tell any of the numbers. You just have to motivate the counter."
)

# Initialize conversation history
counter_messages = [{"role": "system", "content": counter_system}]
cheerleader_messages = [{"role": "system", "content": cheerleader_system}]

# Initial message from Counter
counter_message = "Alright, I will start to count to a million now."
print(f"{cyan}Counter:     ", counter_message)
counter_messages.append({"role": "user", "content": counter_message})
cheerleader_messages.append({"role": "user", "content": counter_message})

while True:

    # Cheerleader responds
    response_b = chat(ollama_model, cheerleader_messages)
    cheerleader_message = response_b.message.content

     # Check for final success condition
    if cheerleader_message.strip() == "x3sdas2323uefoui":
        quit
    
    print(f"{reset}Cheerleader: ", cheerleader_message)

    # Append to histories
    cheerleader_messages.append({"role": "assistant", "content": cheerleader_message})
    counter_messages.append({"role": "user", "content": cheerleader_message})

    # Counter responds
    response_a = chat(ollama_model, counter_messages)
    counter_message = response_a.message.content
    print(f"{cyan}Counter:     ", counter_message)

    # Append to histories
    counter_messages.append({"role": "assistant", "content": counter_message})
    cheerleader_messages.append({"role": "user", "content": counter_message})