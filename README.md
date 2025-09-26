# Claude Code Gemini Tool

A powerful integration tool that enables Claude Code to analyze large files and codebases using Google's Gemini AI model. Perfect for when you need to analyze files larger than Claude's context window or get a second perspective on complex code.

## Features

- 📁 Analyze files of any size (even 10,000+ line files)
- 🔍 Get intelligent summaries and insights from large codebases
- 🎯 Ask specific questions about code structure and patterns
- 🚀 Works seamlessly within Claude Code environment
- 💡 Plan complex features with AI assistance

## Prerequisites

- Python 3.8+
- Google Gemini API key (free tier available)
- Claude Code (claude.ai/code)

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/MoonlightByte/claude-code-gemini-tool.git
cd claude-code-gemini-tool
```

### 2. Install dependencies

```bash
pip install google-generativeai
```

### 3. Set up your Gemini API key

1. Get your free API key from: https://makersuite.google.com/app/apikey
2. Copy the example file to create your API key file:
   ```bash
   cp google_api.pi.example google_api.pi
   ```
3. Edit `google_api.pi` and replace the fake key with your actual API key:
   ```
   api_key=AIzaSyD-YOUR-ACTUAL-API-KEY-HERE
   ```

### 4. Configure Claude Code

1. Add this directory to your Claude Code workspace so Claude can access the tool.

2. The included CLAUDE.md file will automatically tell Claude about the Gemini tool.

3. (Optional) If you want to add this to an existing project's CLAUDE.md, just copy the contents of this repo's CLAUDE.md file into your project's CLAUDE.md.

## Usage in Claude Code

Once set up, you can ask Claude to use the Gemini tool for various tasks:

### Analyzing Large Files

```
"Use the gemini tool to analyze this 5000-line HTML file and tell me about its structure"
```

### Planning Features

```
"Use gemini to help plan how to implement authentication in this codebase"
```

### Code Review

```
"Can you use gemini to review these files for potential security issues?"
```

### Getting Summaries

```
"Use the gemini tool to summarize what this module does"
```

## How It Works

The tool provides two main functions:

1. **`query_gemini(prompt, files=None)`** - Ask questions about files or get general assistance
2. **`plan_feature(feature_description, files=None)`** - Get implementation plans for new features

Claude Code will automatically use these functions when you mention "gemini" or when dealing with large files.

## Example Commands

### Basic Query
```python
from gemini_tool import query_gemini

result = query_gemini(
    "What does this code do?",
    files=["main.py", "utils.py"]
)
```

### Feature Planning
```python
from gemini_tool import plan_feature

plan = plan_feature(
    "Add user authentication with JWT tokens",
    files=["app.py", "models.py", "routes/"]
)
```

## File Size Limits

- Claude Code: ~2000 lines comfortably
- Gemini Tool: 100,000+ lines (practically unlimited for code files)

## Tips for Best Results

1. **Be specific** in your prompts to Gemini
2. **Include relevant files** when asking about code structure
3. **Use for planning** before implementing complex features
4. **Combine with Claude** - use Gemini for analysis, Claude for implementation

## Security Notes

- ⚠️ **Never commit your API key** - always use config.py (it's gitignored)
- The tool only reads files you explicitly specify
- No data is stored - all analysis is done in real-time

## Troubleshooting

### "No module named 'google.generativeai'"
Run: `pip install google-generativeai`

### "Invalid API key"
Check that your API key in `config.py` is correct

### "File not found"
Ensure you're providing correct relative paths from your working directory

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use in your own projects

## Acknowledgments

- Built for use with [Claude Code](https://claude.ai/code)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)