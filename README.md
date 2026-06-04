# strongshrew

Generate Obsidian markdown search links for a query across 26 platforms.

```sh
# generate search links (stdout)
uv run --no-active --project /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew "focaccia sourdough"

# copy to clipboard only, no stdout
uv run --no-active --project /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew --clipboard "focaccia sourdough"

# copy to clipboard and print to stdout
uv run --no-active --project /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew --clipboard --tee "focaccia sourdough"

# run from within the project directory
uv run --no-active strongshrew "sourdough bread"

# using --directory instead of --project
uv run --no-active --directory /Users/mtm/pdev/taylormonacelli/strongshrew strongshrew "cast iron skillet"
```
