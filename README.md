# strongshrew

Generate Obsidian markdown search links for a query across 26 platforms.

```sh
# generate search links (stdout)
uvx --from git+https://github.com/gkwa/strongshrew strongshrew focaccia sourdough

# exact phrase search ("focaccia sourdough" not focaccia sourdough)
uvx --from git+https://github.com/gkwa/strongshrew strongshrew --exact focaccia sourdough

# copy to clipboard only, no stdout
uvx --from git+https://github.com/gkwa/strongshrew strongshrew --clipboard focaccia sourdough

# copy to clipboard and print to stdout
uvx --from git+https://github.com/gkwa/strongshrew strongshrew --clipboard --tee focaccia sourdough
```
