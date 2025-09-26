# Minimal CLAUDE.md Integration

Add this section to your project's CLAUDE.md file:

```markdown
## Gemini Integration

For large-context analysis (files >2000 lines):
```python
from gemini_tool import query_gemini, plan_feature
result = query_gemini("Analyze this", files=["large_file.html"])
```
```

That's it! This minimal addition tells Claude Code that the Gemini tool is available for analyzing large files.