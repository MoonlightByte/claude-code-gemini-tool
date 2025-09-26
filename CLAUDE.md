# CLAUDE.md

## Gemini Integration

Use Gemini for analyzing large files (>2000 lines) or entire codebases that exceed your context window.

### Available Functions

```python
from gemini_tool import query_gemini, plan_feature

# Analyze files with specific questions
result = query_gemini("What does this code do?", files=["main.py", "utils.py"])

# Plan new features based on existing code
plan = plan_feature("Add user authentication", files=["app.py", "models/"])

# Analyze without files (general questions)
result = query_gemini("How should I structure a REST API?")
```

### When to Use
- User mentions "gemini" or "use gemini"
- Files are over 2000 lines
- Analyzing entire directories/projects
- Need comprehensive feature planning
- User asks to analyze files you can't fully load

### Notes
- `files` parameter accepts single files, lists, or directories
- Rate limited to 2 RPM (free tier) - tool handles delays automatically
- Gemini excels at analysis, you excel at implementation