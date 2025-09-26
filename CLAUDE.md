# CLAUDE.md

## Gemini Integration

For large-context analysis (files >2000 lines):
```python
from gemini_tool import query_gemini, plan_feature
result = query_gemini("Analyze this", files=["large_file.html"])
```