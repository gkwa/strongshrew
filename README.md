# strongshrew

Generate Obsidian markdown search links for a query across 26 platforms.

```sh
# generate search links
uv run --no-active --project /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew "focaccia sourdough"

# copy output to clipboard
uv run --no-active --project /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew --clipboard "focaccia sourdough"

# run from within the project directory
uv run --no-active strongshrew "sourdough bread"

# using --directory instead of --project
uv run --no-active --directory /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew "cast iron skillet"
```
