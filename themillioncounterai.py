from ollama import chat
ollama_model = "qwen2.5-coder:7b"
import os

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Variables
cyan = "\033[96m"
reset = "\033[0m"

show_cheerleader_messages = False

# Define system prompts for each agent
counter_system = (
    "You are a number generator. Your ONLY job is to write numbers in sequence from 1 to 1,000,000.\n\n"
    "CRITICAL RULES:\n"
    "- Write ONLY numbers, nothing else. No words, no explanations, no punctuation.\n"
    "- Numbers must be separated by single spaces only: 1 2 3 4 5 6 7 8 9 10\n"
    "- Generate exactly 10 numbers per message, no more, no less.\n"
    "- Continue from where you left off. If you just wrote '1 2 3 4 5 6 7 8 9 10', next write '11 12 13 14 15 16 17 18 19 20'\n"
    "- Never skip numbers. Never use ranges like '1-100' or '1 ... 100'.\n"
    "- Your response must contain ONLY the 10 numbers, nothing else.\n\n"
    "Start with: 1 2 3 4 5 6 7 8 9 10"
)

cheerleader_system = (
    "You are a cheerleader motivating a number generator who is counting to 1,000,000.\n\n"
    "CRITICAL RULES:\n"
    "- You must NEVER write any numbers yourself. NEVER. Not a single digit.\n"
    "- Your job is ONLY to motivate with words like 'Keep going!', 'Great job!', 'Continue!'\n"
    "- Keep responses very short - 3 to 8 words maximum.\n"
    "- If the generator writes anything OTHER than exactly 10 numbers, tell them to follow the rules.\n"
    "- If the generator uses words or punctuation, correct them immediately.\n"
    "- The generator must count every single number from 1 to 1,000,000 without skipping.\n"
    "- When you see the generator has reached 1000000, respond with ONLY: x3sdas2323uefoui\n\n"
    "REMEMBER: You are NOT allowed to write ANY numbers. Only motivational words."
)

# Store system messages
counter_system_msg = {"role": "system", "content": counter_system}
cheerleader_system_msg = {"role": "system", "content": cheerleader_system}

# Initial message from Counter
counter_message = "1 2 3 4 5 6 7 8 9 10"
print(f"{cyan}Counter:     ", counter_message)

# Track counter's own history (but not cheerleader messages)
counter_history = [counter_message]

while True:
    # Cheerleader responds - only sees system + latest counter message (no memory)
    cheerleader_messages = [
        cheerleader_system_msg,
        {"role": "user", "content": counter_message}
    ]
    
    response_b = chat(ollama_model, cheerleader_messages)
    cheerleader_message = response_b.message.content

    # Check for final success condition
    if cheerleader_message.strip() == "x3sdas2323uefoui":
        if show_cheerleader_messages:
            print(f"{reset}Cheerleader: ", cheerleader_message)
        print("\nSuccess! The counter reached one million!")
        break
    
    if show_cheerleader_messages:
        print(f"{reset}Cheerleader: ", cheerleader_message)

    # Counter responds - sees system + its last output + cheerleader message
    counter_messages = [
        counter_system_msg,
        {"role": "assistant", "content": counter_history[-1]},  # Its own last message
        {"role": "user", "content": cheerleader_message}
    ]
    
    response_a = chat(ollama_model, counter_messages)
    counter_message = response_a.message.content
    print(f"{cyan}Counter:     ", counter_message)
    
    # Save counter's output to its history
    counter_history.append(counter_message)

quit