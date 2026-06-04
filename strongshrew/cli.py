import argparse
import importlib.metadata
import sys
import urllib.parse

import strongshrew.platforms as platforms_module


def generate(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    lines = [f"{query} — search links across platforms", ""]
    for name, template in platforms_module.PLATFORMS:
        url = template.format(query=encoded)
        lines.append(f"- [{query} on {name}]({url})")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate cross-platform search links in Obsidian markdown"
    )
    parser.add_argument("query", help="Search term")
    parser.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Copy output to clipboard",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=importlib.metadata.version("strongshrew"),
    )
    args = parser.parse_args()

    output = generate(args.query)
    sys.stdout.write(output)

    if args.clipboard:
        import pyperclip  # type: ignore[import-untyped]

        pyperclip.copy(output)


if __name__ == "__main__":
    main()
