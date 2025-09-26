# CLAUDE.md - Instructions for Claude Code

This file helps Claude Code understand how to use the Gemini tool effectively.

## Tool Overview

The Gemini tool allows you to analyze large files and codebases that exceed your context window using Google's Gemini AI model. It's particularly useful for:
- Files over 2000 lines
- Analyzing entire project structures
- Getting implementation plans for complex features
- Reviewing large HTML/CSS files
- Understanding database schemas

## When to Use the Gemini Tool

Use the Gemini tool when:
- User mentions "gemini" or "use gemini"
- Files are too large for your context (>2000 lines)
- User needs analysis of multiple large files
- Planning complex features before implementation
- User explicitly asks for a second opinion

## How to Use

### Basic Query
```python
from gemini_tool import query_gemini

result = query_gemini(
    "What patterns are used in this codebase?",
    files=["app.py", "models/", "routes/"]
)
print(result)
```

### Feature Planning
```python
from gemini_tool import plan_feature

plan = plan_feature(
    "Add real-time notifications using WebSockets",
    files=["app.py", "static/js/main.js", "templates/"]
)
print(plan)
```

### Analyzing Large Files
```python
result = query_gemini(
    "Summarize the structure and main components of this file",
    files=["large_file_with_10000_lines.html"]
)
```

## Important Notes

1. **Rate Limits**: Gemini has rate limits (2 RPM for free tier). The tool handles this automatically with delays.

2. **File Paths**: Always use relative paths from the current working directory.

3. **Response Format**: Gemini returns text responses. Parse them appropriately for the user.

4. **Complementary Use**: You (Claude) are better at writing code. Gemini is better at analyzing large amounts of existing code. Use both strengths.

## Common Patterns

### When user says "analyze this large file"
```python
# Automatically use Gemini for files you can't fully load
result = query_gemini(
    "Provide a comprehensive analysis of this file's structure, purpose, and key components",
    files=[user_specified_file]
)
```

### When planning a new feature
```python
# Get Gemini's plan first
plan = plan_feature(
    user_feature_description,
    files=relevant_existing_files
)
# Then you implement based on the plan
```

### When user needs a code review
```python
result = query_gemini(
    "Review this code for best practices, potential issues, and improvements",
    files=files_to_review
)
```

## Error Handling

If you encounter errors:
- "No google_api.pi file" → Tell user to create one with their API key
- "Rate limit exceeded" → Wait and retry (handled automatically)
- "File not found" → Check the file path is correct
- "Invalid API key" → User needs to check their API key

## Best Practices

1. **Be Specific**: Give Gemini specific questions, not vague requests
2. **Include Context**: Tell Gemini what you're trying to achieve
3. **Use for Analysis**: Let Gemini analyze, you implement
4. **Batch Requests**: Ask multiple questions in one query when possible
5. **Clean Up**: The tool auto-cleans uploaded files, but be mindful of usage

## Example User Interactions

**User**: "This HTML file is 5000 lines, can you understand its structure?"
**You**: "I'll use the Gemini tool to analyze this large file for you..."
```python
result = query_gemini(
    "Analyze the structure, identify main sections, and list all interactive components",
    files=["large.html"]
)
```

**User**: "Help me add authentication to this Flask app"
**You**: "Let me use Gemini to create a comprehensive plan based on your existing code..."
```python
plan = plan_feature(
    "Add JWT-based authentication with login, logout, and protected routes",
    files=["app.py", "models.py", "requirements.txt"]
)
```

## Remember

- You're working together with Gemini, not competing
- Gemini excels at analysis of large codebases
- You excel at writing clean, correct implementation code
- Always explain to the user when and why you're using Gemini