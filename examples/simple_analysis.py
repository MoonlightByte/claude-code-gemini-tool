#!/usr/bin/env python3
"""
Simple Example: Analyze D&D Module Files

Shows basic usage of the Gemini tool to analyze game content.
"""

import sys
import os

# Add parent directory to path so we can import gemini_tool
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_tool import query_gemini

# Simple analysis of a game module
print("Analyzing D&D Module Structure...")
print("=" * 50)

result = query_gemini(
    prompt="Summarize the key elements of this D&D module - what's the main quest and who are the important NPCs?",
    files=["modules/Shadows_of_Kharos/module_plot.json"]  # Adjust path as needed
)

print(result)