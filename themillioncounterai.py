from ollama import chat
import os
import random
import resource

# Configuration
MODEL = "qwen2.5-coder:7b"
SHOW_USAGE = True

# Terminal colors
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Style functions
os.system('cls' if os.name == 'nt' else 'clear')

print(f"""{CYAN}
▐                 ▌                     
▜▀                ▛▀▖                ▞▀▖
▐ ▖               ▌ ▌                ▛▀ 
 ▀                ▘ ▘                ▝▀▘
▗▌    ▞▀▖   ▞▀▖   ▞▀▖    ▞▀▖   ▞▀▖   ▞▀▖
 ▌    ▌▞▌   ▌▞▌   ▌▞▌    ▌▞▌   ▌▞▌   ▌▞▌
 ▌    ▛ ▌   ▛ ▌   ▛ ▌    ▛ ▌   ▛ ▌   ▛ ▌
▝▀    ▝▀    ▝▀    ▝▀     ▝▀    ▝▀    ▝▀ 
                ▐                     ▗ 
▞▀▖ ▞▀▖ ▌ ▌ ▛▀▖ ▜▀  ▞▀▖ ▙▀▖       ▝▀▖ ▄ 
▌ ▖ ▌ ▌ ▌ ▌ ▌ ▌ ▐ ▖ ▛▀  ▌         ▞▀▌ ▐ 
▝▀  ▝▀  ▝▀▘ ▘ ▘  ▀  ▝▀▘ ▘         ▝▀▘ ▀▘

""")

MODEL_INPUT = input(f"{RESET}Your preferred Ollama Model (>7b recommended, press Enter for default): ").strip()
if MODEL_INPUT == "" or MODEL_INPUT.lower() == "d":
    MODEL = "qwen2.5-coder:7b"
    print(f"Using default model: {MODEL}")
else:
    MODEL = MODEL_INPUT
    print(f"Using model: {MODEL}")

usage_input = input("Do you want to see your hardware usage? (y/n): ").strip().lower()
if usage_input in ["y", "yes", "true", "t"]:
    SHOW_USAGE = True
    print("Hardware usage display: ENABLED")
    # Check if psutil is available for Windows
    if os.name == 'nt':
        try:
            import psutil
        except ImportError:
            print(f"{YELLOW}Warning: psutil not installed. Installing for Windows compatibility...{RESET}")
            print("Run: pip install psutil")
            SHOW_USAGE = False
else:
    SHOW_USAGE = False
    print("Hardware usage display: DISABLED")

print(CYAN)

# System prompts
COUNTER_PROMPT = """You are a number generator. Your ONLY job is to count up numbers in sequence from 1 to 1,000,000.

CRITICAL RULES:
- Write ONLY numbers, nothing else. No words, no explanations, no punctuation.
- Numbers must be separated by single spaces only
- Generate exactly 20 numbers per message, no more, no less.
- Continue from where you left off. If you just wrote '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20', next write '21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40'
- Never skip numbers. Never use ranges like '1-100' or '1 ... 100'.
- Your response must contain ONLY the 20 numbers separated by spaces, nothing else.
- DO NOT write more than 20 numbers. DO NOT write less than 20 numbers. EXACTLY 20 numbers.

Example of correct format: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"""

def print_usage(iteration, clear=True):
    """Print current memory usage at the bottom of terminal"""
    if clear:
        # Move cursor to bottom of terminal
        print("\n" * 2)
    
    if os.name != 'nt':
        usage = resource.getrusage(resource.RUSAGE_SELF)
        memory_mb = usage.ru_maxrss / 1024
        cpu_time = usage.ru_utime + usage.ru_stime
        print(f"{CYAN}{'─' * 60}")
        print(f"Iteration: {iteration:,} | Memory: {memory_mb:.1f}MB | CPU Time: {cpu_time:.1f}s")
        print(f"{'─' * 60}{RESET}")
    else:
        import psutil
        process = psutil.Process()
        memory_mb = process.memory_info().rss / 1024 / 1024
        cpu_percent = process.cpu_percent(interval=0.1)
        print(f"{CYAN}{'─' * 60}")
        print(f"Iteration: {iteration:,} | Memory: {memory_mb:.1f}MB | CPU: {cpu_percent:.1f}%")
        print(f"{'─' * 60}{RESET}")

class Cheerleader:
    """Validates counter output and provides appropriate feedback"""
    
    motivations = [
        "Continue counting. Write the next 20 numbers in sequence.",
        "Keep going. Generate the next 20 consecutive numbers.",
        "Good progress. Continue with the next 20 numbers.",
        "Excellent. Proceed with the next 20 numbers in order.",
        "Well done. Now write the next 20 consecutive numbers."
    ]
    
    @staticmethod
    def check_counter_output(counter_output):
        """
        Validates the counter output and returns appropriate feedback message.
        Returns tuple: (message, is_complete)
        """
        counter_output_split = counter_output.strip().split()
        
        # Check if we've reached 1,000,000
        try:
            if any(int(num) == 1000000 for num in counter_output_split):
                return ("COMPLETE", True)
        except ValueError:
            pass
        
        # Validate that we have exactly 20 numbers
        if len(counter_output_split) != 20:
            return (
                f"{RED}ERROR: You must write exactly 20 numbers. You wrote {len(counter_output_split)}. "
                f"Please write the next 20 consecutive numbers starting from where you left off.{RESET}",
                False
            )
        
        # Try to convert all to integers
        try:
            numbers = [int(num) for num in counter_output_split]
        except ValueError:
            return (
                f"{RED}ERROR: Your output contains non-numeric values. "
                f"Write only numbers separated by spaces. Provide the next 20 consecutive numbers.{RESET}",
                False
            )
        
        # Check if numbers are consecutive (difference of 1 between each)
        for i in range(len(numbers) - 1):
            if numbers[i + 1] - numbers[i] != 1:
                return (
                    f"{RED}ERROR: Numbers are not consecutive. "
                    f"Found gap between {numbers[i]} and {numbers[i + 1]}. "
                    f"Write the next 20 consecutive numbers starting from {numbers[-1] + 1}.{RESET}",
                    False
                )
        
        # Check if the range is exactly 19 (20 consecutive numbers: last - first = 19)
        if numbers[-1] - numbers[0] != 19:
            return (
                f"{RED}ERROR: The numbers don't form a proper sequence of 20. "
                f"Write exactly 20 consecutive numbers starting from {numbers[-1] + 1}.{RESET}",
                False
            )
        
        # Everything is correct - return a random motivation
        return (random.choice(Cheerleader.motivations), False)

def main():
    iteration = 0
    
    # Initialize with 20 numbers
    counter_msg = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
    counter_history = [counter_msg]
    max_history = 1  # Only keep last 1 entry for minimal memory
    
    print(f"{CYAN}{counter_msg}{RESET}")
    
    cheerleader_msg = "Continue counting. Write the next 20 numbers in sequence."

    while True:
        # Counter responds with limited context
        counter_response = chat(MODEL, [
            {"role": "system", "content": COUNTER_PROMPT},
            {"role": "assistant", "content": counter_history[-1]},
            {"role": "user", "content": cheerleader_msg}
        ], options={"num_ctx": 512})  # Limit context window to 512 tokens
        
        counter_msg = counter_response.message.content.strip()
        counter_history.append(counter_msg)
        
        # Keep history size limited
        if len(counter_history) > max_history:
            counter_history.pop(0)
        
        iteration += 1
        
        print(f"{CYAN}{counter_msg}{RESET}")

        # Check if complete and get feedback (but don't display it)
        cheerleader_msg, is_complete = Cheerleader.check_counter_output(counter_msg)
        
        if is_complete:
            print(f"\n{CYAN}{'='*60}")
            print("SUCCESS! The counter reached ONE MILLION!")
            print(f"{'='*60}{RESET}")
            print(f"Total iterations: {iteration}")
            print(f"Total numbers generated: {iteration * 20}")
            break
        
        # Show usage stats every 100 iterations
        if SHOW_USAGE and iteration % 100 == 0:
            print_usage()
        
        # Clear old messages periodically to free memory
        if iteration % 1000 == 0:
            import gc
            gc.collect()  # Force garbage collection

if __name__ == "__main__":
    main()