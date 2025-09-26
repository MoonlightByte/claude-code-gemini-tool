#!/usr/bin/env python3
"""
Example: Analyze D&D Game Module with Gemini

Simple example showing how to use the Gemini tool to analyze game files
that are too large for Claude's context window.
"""

import sys
import os

# Add parent directory to path so we can import gemini_tool
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_tool import query_gemini, plan_feature

# Example 1: Analyze the structure of game modules
print("=" * 60)
print("EXAMPLE 1: Analyze Module Structure")
print("=" * 60)

result = query_gemini(
    "What are the main locations and NPCs in these module files? List them clearly.",
    files=[
        "/mnt/c/dungeon_master_v1/modules/Shadows_of_Kharos/module_plot.json",
        "/mnt/c/dungeon_master_v1/modules/Shadows_of_Kharos/map_MRV001.json", 
        "/mnt/c/dungeon_master_v1/modules/Shadows_of_Kharos/map_DC001.json"
    ]
)
print(result)

# Example 2: Get implementation plan for a new feature
print("\n" + "=" * 60)
print("EXAMPLE 2: Plan New Feature")
print("=" * 60)

plan = plan_feature(
    "Add a new side quest involving a mysterious merchant to this module",
    files=["/mnt/c/dungeon_master_v1/modules/Shadows_of_Kharos/module_plot.json"]
)
print(plan)

# Example 3: Analyze large HTML file
print("\n" + "=" * 60)
print("EXAMPLE 3: Analyze Large HTML Interface")
print("=" * 60)

analysis = query_gemini(
    "Analyze this game interface HTML and identify the main UI components and their purposes",
    files=["/mnt/c/dungeon_master_v1/templates/game_interface.html"]
)
print(analysis)

print("\n" + "=" * 60)
print("Analysis complete!")
print("=" * 60)