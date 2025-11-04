# TSX to Jupyter HTML Conversion Note

**Issue**: TSX/React files with CDN dependencies don't render in Jupyter notebooks due to security restrictions.

**Solution**: Use pure vanilla JavaScript instead of React.

## Key Changes Made:
1. Removed React, ReactDOM, Babel dependencies
2. Converted JSX to plain HTML + vanilla JS
3. Replaced `useState`, `useEffect` with simple variables
4. Used direct DOM manipulation instead of React rendering
5. Styled with CSS similar to `partition-explanation.html` (Jupyter-friendly)

**Result**: `quicksort-viz.html` now works perfectly in Jupyter using `IPython.display.HTML()`
