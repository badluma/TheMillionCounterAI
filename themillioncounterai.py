from ollama import chat
import os
import random

# Configuration
MODEL = "qwen2.5-coder:7b"
SHOW_CHEERLEADER = True

# Terminal colors
CYAN = "\033[96m"
RESET = "\033[0m"

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# System prompts
COUNTER_PROMPT = """You are a number generator. Your ONLY job is to write numbers in sequence from 1 to 1,000,000.

CRITICAL RULES:
- Write ONLY numbers, nothing else. No words, no explanations, no punctuation.
- Numbers must be separated by single spaces only: 1 2 3 4 5 6 7 8 9 10
- Generate exactly 10 numbers per message, no more, no less.
- Continue from where you left off. If you just wrote '1 2 3 4 5 6 7 8 9 10', next write '11 12 13 14 15 16 17 18 19 20'
- Never skip numbers. Never use ranges like '1-100' or '1 ... 100'.
- Your response must contain ONLY the 10 numbers, nothing else. 
- You do everything that the user says, as long as it matches your instructions. 

Start with: 1 2 3 4 5 6 7 8 9 10"""

class cheerleader:
    cheerleader_msg = ""

    motivations = ["Keep going"]
    warnings = ["You did something wrong! Try again from last time!"]
    
    def check_counter_output(counter_output):
        previous_last_number = None
        global cheerleader_msg
        counter_output_split = counter_output.split()
        previous_last_number = 0
        
        # Convert specific elements to integers if needed
        try:
            if (int(counter_output_split[9]) - int(counter_output_split[0])) == int(counter_output_split[0]) and previous_last_number + 1 == int(converter_output_split[0]):
                cheerleader_msg = cheerleader.motivations[random.randint(0, len(cheerleader.motivations))]
                if any(int(i) == 1000000 for i in counter_output):
                    cheerleader_msg = "x3sdas2323uefoui"
        except ValueError:
            cheerleader_msg = "Invalid input: Please make sure each number is separated by a single space."

def main():
    counter_msg = ""
    global cheerleader_msg
    # Initialize
    counter_msg = "1 2 3 4 5 6 7 8 9 10"
    counter_history = [counter_msg]
    
    print(f"{CYAN}Counter:     {counter_msg}{RESET}")
    
    cheerleader_msg = "Keep going until 1 million without skipping any numbers with only 10 numbers in one string!"
    if SHOW_CHEERLEADER:
        print(f"Cheerleader: {cheerleader_msg}")

    while True:
        # Counter responds
        counter_response = chat(MODEL, [
            {"role": "system", "content": COUNTER_PROMPT},
            {"role": "assistant", "content": counter_history[-1]},
            {"role": "user", "content": cheerleader_msg}
        ])
        counter_msg = counter_response.message.content
        counter_history.append(counter_msg)
        
        print(f"{CYAN}Counter:     {counter_msg}{RESET}")

        # Check if complete
        cheerleader.check_counter_output(counter_msg)
        if cheerleader_msg == "x3sdas2323uefoui":
            if SHOW_CHEERLEADER:
                print(f"Cheerleader: {cheerleader_msg}")
            print("\nSuccess! The counter reached one million!")
            break
        
        if SHOW_CHEERLEADER:
            print(f"Cheerleader: {cheerleader_msg}")


main()