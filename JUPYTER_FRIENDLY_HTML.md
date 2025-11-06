# Jupyter-Friendly HTML Guidelines

## Acceptance Criteria Checklist

A standalone HTML file is **Jupyter-friendly** when it meets ALL of these criteria:

### ✅ Structure Requirements

- [ ] **No document tags**: Remove `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags
- [ ] **Single wrapper div**: Wrap entire content in one uniquely-named container div (e.g., `<div class="my-viz-wrapper">`)
- [ ] **Self-contained**: All CSS in `<style>` tag, all JS in `<script>` tag

### ✅ CSS Requirements

- [ ] **Scoped selectors**: ALL CSS selectors must start with wrapper class (`.my-viz-wrapper h1`, `.my-viz-wrapper .button`)
- [ ] **Force visibility**: Add `!important` to critical styles, especially:
  - `color: #value !important;`
  - `opacity: 1 !important;`
- [ ] **Universal rule**: Add `.my-viz-wrapper * { color: #2c3e50 !important; opacity: 1 !important; }`

### ✅ JavaScript Requirements

- [ ] **Self-executing function**: Wrap entire script in `(function() { ... })();`
- [ ] **Expose functions**: If using inline `onclick` handlers, expose functions to global scope:
  ```javascript
  window.myFunction = myFunction;
  ```
- [ ] **OR use addEventListener**: Replace inline handlers with event listeners (preferred)

### ✅ Final Structure Template

```html
<style>
    .my-viz-wrapper { /* wrapper styles */ }
    .my-viz-wrapper * { color: #2c3e50 !important; opacity: 1 !important; }
    .my-viz-wrapper h1 { color: #333 !important; }
    .my-viz-wrapper .button { /* scoped styles */ }
    /* All other selectors prefixed with .my-viz-wrapper */
</style>

<div class="my-viz-wrapper">
    <!-- Your HTML content here -->
</div>

<script>
(function() {
    // Your JavaScript code here
    
    // Expose functions for onclick handlers (if needed)
    window.myFunction = myFunction;
})();
</script>
```

## Quick Test

Load in Jupyter with:
```python
from IPython.display import HTML
with open('my_viz.html', 'r') as f:
    html_content = f.read()
HTML(html_content)
```

**Pass criteria**: 
- ✅ Visualizations render correctly
- ✅ All text is visible (not transparent/wrong color)
- ✅ Interactive elements work (buttons, sliders)
- ✅ No console errors
- ✅ No style conflicts with notebook theme
