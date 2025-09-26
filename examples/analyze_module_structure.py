#!/usr/bin/env python3
"""
Example: Analyze D&D Module Structure with Gemini

This script demonstrates using the Gemini tool to analyze the structure
of a D&D module, including NPCs, locations, encounters, and plot hooks.
Perfect for understanding large game modules that exceed Claude's context window.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_tool import query_gemini, plan_feature

def analyze_module_structure(module_path):
    """Analyze the complete structure of a D&D module"""
    
    print(f"Analyzing module at: {module_path}")
    print("-" * 50)
    
    # Analyze the module's overall structure
    structure_prompt = """
    Please analyze this D&D module and provide:
    1. Module name and main theme
    2. Total number of areas/locations
    3. Key NPCs and their roles
    4. Main quest hooks and objectives
    5. Notable encounters or challenges
    6. Any unique features or mechanics
    
    Format the response in a clear, organized way.
    """
    
    try:
        # Get all JSON files in the module
        module_files = []
        for root, dirs, files in os.walk(module_path):
            for file in files:
                if file.endswith('.json'):
                    module_files.append(os.path.join(root, file))
        
        if not module_files:
            print("No JSON files found in module directory")
            return
        
        # Analyze module structure
        print("\n[1/3] Analyzing Module Structure...")
        result = query_gemini(structure_prompt, files=module_files[:10])  # Limit to first 10 files for demo
        print(result)
        
        # Analyze NPCs specifically
        print("\n[2/3] Analyzing NPCs in Module...")
        npc_prompt = """
        List all NPCs found in this module with:
        - Name and role
        - Location where they can be found
        - Their significance to the story
        - Any special abilities or items
        """
        
        npc_files = [f for f in module_files if 'npc' in f.lower() or 'character' in f.lower()]
        if npc_files:
            npc_result = query_gemini(npc_prompt, files=npc_files[:5])
            print(npc_result)
        
        # Get improvement suggestions
        print("\n[3/3] Getting Module Improvement Suggestions...")
        improvement_result = plan_feature(
            "Add more depth to this D&D module with additional side quests and NPC interactions",
            files=module_files[:5]
        )
        print(improvement_result)
        
        print("\n" + "="*50)
        print("Analysis complete!")
        
    except FileNotFoundError:
        print(f"Error: Module path not found: {module_path}")
    except Exception as e:
        print(f"Error during analysis: {e}")

def analyze_single_area(area_file):
    """Analyze a single area file in detail"""
    
    print(f"\nAnalyzing area: {area_file}")
    print("-" * 30)
    
    area_prompt = """
    Analyze this D&D area/location and provide:
    1. Location name and description
    2. Important features or landmarks
    3. NPCs present
    4. Possible encounters
    5. Connected areas (exits)
    6. Any treasure or secrets
    """
    
    try:
        result = query_gemini(area_prompt, files=[area_file])
        print(result)
    except Exception as e:
        print(f"Error analyzing area: {e}")

if __name__ == "__main__":
    # Example 1: Analyze a complete module
    module_path = "../../modules/Goblin_Caves"
    
    if os.path.exists(module_path):
        analyze_module_structure(module_path)
    else:
        print(f"Module not found at {module_path}")
        print("Trying alternate path...")
        
        # Try from different working directory
        alt_path = "modules/Goblin_Caves"
        if os.path.exists(alt_path):
            analyze_module_structure(alt_path)
        else:
            print("Creating demo with sample paths...")
            print("\nDemo output (paths would need to be adjusted):")
            print("="*50)
            print("This script would analyze:")
            print("- Module metadata and plot")
            print("- All area JSON files")  
            print("- NPC definitions")
            print("- Encounter tables")
            print("- And provide improvement suggestions")
    
    # Example 2: Analyze a specific area
    print("\n" + "="*50)
    print("SINGLE AREA ANALYSIS EXAMPLE")
    print("="*50)
    
    area_path = "../../modules/Goblin_Caves/areas/HH001.json"
    if os.path.exists(area_path):
        analyze_single_area(area_path)
    else:
        # Try alternate path
        alt_area = "modules/Goblin_Caves/areas/HH001.json"
        if os.path.exists(alt_area):
            analyze_single_area(alt_area)