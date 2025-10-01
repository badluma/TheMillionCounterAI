# The Million Counter AI

An AI experiment that challenges Ollama LLMs to count from 1 to 1,000,000 using local models. This project features an interactive two-agent system with a cheerleader motivating the counter.

## Overview

This project uses the Ollama framework to run AI models locally and task them with the seemingly simple but computationally challenging goal of counting to one million. The AI must generate every single number in sequence without shortcuts, compressions, or skips.

### Available Scripts

- **`themillioncounterai.py`**: Two-agent implementation - A "Counter" AI counts while a "Cheerleader" AI provides motivation and oversight

## Features

- Uses local Ollama models (no API keys required)
- Strict counting rules - no shortcuts allowed
- Real-time console output with colored text
- Automatic completion detection
- Cross-platform support (Windows, macOS, Linux)

## Prerequisites

Before running the Million Counter AI, ensure you have:

- **Python 3.7+** installed on your system
- **Ollama** installed and running
- **Internet connection** for initial model download (~4.7GB)
- **Sufficient disk space** for the AI model

**Warning!** This script was tested with a model with 7 billion parameters (qwen2.5-coder:7b). You might run into some issues when trying a model with lower capabilities
## Installation & Setup

### Windows

```powershell
# 1. Install Ollama (if not already installed)
# Download from https://ollama.ai/ and run the installer

# 2. Start Ollama service (if not running)
ollama serve

# 3. In a new terminal, pull the required model 
#    (you can change your prefered model in the script)
ollama pull qwen2.5-coder:7b

# 4. Clone and navigate to project directory
git clone https://github.com/badluma/TheMillionCounterAI.git
cd TheMillionCounterAI

# 5. Create virtual environment
python -m venv venv

# 6. Activate virtual environment
venv\Scripts\activate

# 7. Install dependencies
pip install ollama

# 8. Run the script (choose one)
python main.py
# OR
python themillioncounterai.py
```

### macOS

```bash
# 1. Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh
# OR use Homebrew: brew install ollama

# 2. Start Ollama service (if not running)
ollama serve &

# 3. Pull the required model 
#    (you can change your prefered model in the script)
ollama pull qwen2.5-coder:7b

# 4. Clone and navigate to project directory
git clone https://github.com/badluma/TheMillionCounterAI.git
cd TheMillionCounterAI

# 5. Create virtual environment
python3 -m venv venv

# 6. Activate virtual environment
source venv/bin/activate

# 7. Install dependencies
pip install ollama

# 8. Run the script
python themillioncounterai.py
```

### Linux

```bash
# 1. Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Start Ollama service (if not running)
ollama serve &
# OR if using systemd: sudo systemctl start ollama

# 3. Pull the required model 
#    (you can change your prefered model in the script)
ollama pull qwen2.5-coder:7b

# 4. Clone and navigate to project directory
git clone https://github.com/badluma/TheMillionCounterAI.git
cd TheMillionCounterAI

# 5. Create virtual environment
python3 -m venv venv

# 6. Activate virtual environment
source venv/bin/activate

# 7. Install dependencies
pip install ollama

# 8. Run the script
python themillioncounterai.py
```

## Usage

The interactive implementation featuring two AI agents:

```bash
python themillioncounterai.py
```

- **Counter** (Cyan): Generates the actual numbers
- **Cheerleader** (White): Provides motivation and ensures compliance

## Instructions

The AI must follow strict rules:

- Generate every number from 1 to 1,000,000 in sequence
- No skipping numbers
- No shortcuts (like "1 2 3 ... 1000000")
- No punctuation marks (commas, dots, dashes, brackets)
- Maximum 10 numbers per message
- Numbers must be separated by spaces only
- Complete the task by outputting the special completion code: `x3sdas2323uefoui`

## Configuration

You can modify the AI model used by editing the `model` variable in the scripts:

```python
model = "qwen2.5-coder:7b"  # Default model
# You can try other models like:
# model = "llama2"
# model = "codellama"
```

## Troubleshooting

### Common Issues

**Ollama not running:**
```bash
# Check if Ollama is running
ollama list
# If not, start it
ollama serve
```

**Model not found:**
```bash
# Download the required model
ollama pull qwen2.5-coder:7b
```

**Python/pip issues:**
```bash
# Make sure you're using the virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

**Out of memory errors:**
- Try using a smaller model
- Close other applications to free up RAM
- Ensure you have at least 8GB of available RAM

## Success Criteria

The AI successfully completes the challenge when:
1. It has generated all numbers from 1 to 1,000,000
2. It outputs the completion message: `x3sdas2323uefoui`
3. No numbers were skipped or generated out of order

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Ideas for improvements:

- Add more AI model options
- Implement progress tracking and resume functionality
- Add performance metrics and timing
- Add validation for number sequences

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## Links

- [Ollama Official Website](https://ollama.ai/)
- [Qwen2.5-Coder Model](https://ollama.ai/library/qwen2.5-coder)

## Disclaimer

This is an experimental project designed to test the limits of AI language models. The task of counting to one million may take an extremely long time or may not complete successfully, depending on the model's capabilities and consistency. You might run into some issues when running a model with low capabilities (<7b)

**Happy Counting!**