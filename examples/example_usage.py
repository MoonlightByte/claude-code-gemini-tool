#!/usr/bin/env python3
"""
Example usage of the Gemini tool for Claude Code
"""

from gemini_tool import query_gemini, plan_feature

# Example 1: Analyze a single file
print("=" * 50)
print("Example 1: Analyzing a single file")
print("=" * 50)

result = query_gemini(
    "What does this script do and what are its main functions?",
    files=["gemini_tool.py"]
)
print(result)

# Example 2: Plan a new feature
print("\n" + "=" * 50)
print("Example 2: Planning a new feature")
print("=" * 50)

plan = plan_feature(
    "Add user authentication with sessions",
    files=["app.py", "models.py"]  # Replace with your actual files
)
print(plan)

# Example 3: Analyze multiple files
print("\n" + "=" * 50)
print("Example 3: Analyzing multiple files")
print("=" * 50)

result = query_gemini(
    "How do these files work together? What's the overall architecture?",
    files=["main.py", "utils.py", "config.py"]  # Replace with your actual files
)
print(result)

# Example 4: Code review
print("\n" + "=" * 50)
print("Example 4: Code review")
print("=" * 50)

result = query_gemini(
    "Review this code for potential bugs, security issues, and improvements",
    files=["app.py"]  # Replace with file to review
)
print(result)

# Example 5: Large file analysis
print("\n" + "=" * 50)
print("Example 5: Large file analysis")
print("=" * 50)

result = query_gemini(
    """This file has over 5000 lines. Please:
    1. Summarize its main purpose
    2. List the major sections/components
    3. Identify any potential issues
    4. Suggest how it could be refactored""",
    files=["large_file.html"]  # Replace with your large file
)
print(result)