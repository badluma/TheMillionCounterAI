# The Million Counter AI

An AI experiment that challenges Ollama LLMs to count from 1 to 1,000,000 using local models. This project tests the limits of AI language models with a seemingly simple but computationally intensive task.

## Overview

This project uses the Ollama framework to run AI models locally and task them with counting to one million. The AI must generate every single number in sequence without shortcuts, compressions, or skips. The system features intelligent validation that monitors the AI's output and provides corrective feedback when needed.

## Features

- Uses local Ollama models (no API keys required)
- Strict counting rules - no shortcuts allowed
- Intelligent output validation with specific error detection
- Real-time console output with colored text
- Optional hardware usage monitoring (memory and CPU time)
- Automatic completion detection
- Memory-efficient design with periodic garbage collection
- Cross-platform support (Windows, macOS, Linux)

## How It Works

The script implements a validation system that:
- Ensures exactly 20 consecutive numbers per output
- Detects and corrects counting errors (skips, non-consecutive numbers, wrong count)
- Provides specific feedback to guide the AI back on track
- Monitors for completion when 1,000,000 is reached

**Warning!** This script was tested with a 7 billion parameter model (qwen2.5-coder:7b). You might encounter issues when using models with lower capabilities.

## Prerequisites

Before running the Million Counter AI, ensure you have:

- **Python 3.7+** installed on your system
- **Ollama** installed and running
- **Internet connection** for initial model download (~4.7GB for default model)
- **Sufficient disk space** for the AI model
- **At least 8GB RAM** recommended for optimal performance

## Installation & Setup

### Windows

```powershell
# 1. Install Ollama (if not already installed)
# Download from https://ollama.ai/ and run the installer

# 2. Install psutil to display hardware stats
pip install psutil

# 3. Start Ollama service (if not running)
ollama serve

# 4. In a new terminal, pull the required model 
#    (you can change your preferred model in the script)
ollama pull qwen2.5-coder:7b

# 5. Clone and navigate to project directory
git clone https://github.com/badluma/TheMillionCounterAI.git
cd TheMillionCounterAI

# 6. Create virtual environment
python -m venv venv

# 7. Activate virtual environment
venv\Scripts\activate

# 8. Install dependencies
pip install ollama

# 9. Run the script
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
#    (you can change your preferred model in the script)
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
#    (you can change your preferred model in the script)
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

Run the script with:

```bash
python themillioncounterai.py
```

### Interactive Setup

When you run the script, you'll be prompted to:

1. **Choose your model**: Press Enter to use the default (qwen2.5-coder:7b) or enter your preferred Ollama model name
2. **Hardware usage monitoring**: Type 'y' to enable memory and CPU time tracking, or 'n' to disable

### Output

- **Cyan text**: Counter output showing the current 20 numbers
- **Hardware stats** (if enabled): Displayed every 100 iterations showing memory usage and CPU time
- **Success message**: Displayed when the counter reaches 1,000,000

## Counting Rules

The AI must follow strict rules:

- Generate every number from 1 to 1,000,000 in sequence
- Output exactly 20 numbers per message
- No skipping numbers
- No shortcuts (like "1-100" or "1 ... 1000")
- No punctuation marks (commas, dots, dashes, brackets)
- Numbers must be separated by single spaces only
- All numbers must be consecutive (each number is exactly 1 more than the previous)

## Configuration

You can modify the AI model by either:

1. **Interactive prompt**: When running the script, enter your preferred model name
2. **Edit the script**: Change the `MODEL` variable in `themillioncounterai.py`:

```python
MODEL = "qwen2.5-coder:7b"  # Default model
# You can try other models like:
# MODEL = "llama3.2:latest"
# MODEL = "mistral:latest"
# MODEL = "codellama:latest"
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
- Disable hardware usage monitoring to reduce overhead

**AI keeps making errors:**
- The validation system provides specific feedback to correct errors
- If errors persist, try a larger model with better instruction-following capabilities
- Consider models with 7B+ parameters for best results

## Success Criteria

The AI successfully completes the challenge when:
1. It has generated all numbers from 1 to 1,000,000
2. All numbers were consecutive with no skips
3. The completion message is displayed showing total iterations and numbers generated

## Performance Notes

- The script uses a limited context window (512 tokens) to reduce memory usage
- History is limited to the last response to minimize memory footprint
- Garbage collection runs every 1000 iterations to free memory
- Hardware usage stats (when enabled) are displayed every 100 iterations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Ideas for improvements:

- Add progress tracking and resume functionality
- Implement checkpoint saving/loading
- Add performance metrics and detailed timing analysis
- Support for different number ranges or counting patterns
- Enhanced error recovery mechanisms
- Progress visualization

## License

This project is open source and available under the [MIT License](LICENSE).

## Links

- [Ollama Official Website](https://ollama.ai/)
- [Qwen2.5-Coder Model](https://ollama.ai/library/qwen2.5-coder)
- [Ollama Python Library](https://github.com/ollama/ollama-python)

## Disclaimer

This is an experimental project designed to test the limits of AI language models. The task of counting to one million may take an extremely long time or may not complete successfully, depending on the model's capabilities and consistency. Models with fewer than 7 billion parameters may struggle with this task.

**Happy Counting!**