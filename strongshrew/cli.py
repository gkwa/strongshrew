import argparse
import importlib.metadata
import sys
import urllib.parse

import strongshrew.platforms as platforms_module


def generate(query: str, exact: bool = False) -> str:
    search_term = f'"{query}"' if exact else query
    encoded = urllib.parse.quote_plus(search_term)
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
    parser.add_argument("query", nargs="+", help="Search term (words joined automatically)")
    parser.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Copy output to clipboard (suppresses stdout)",
    )
    parser.add_argument(
        "--exact",
        "-e",
        action="store_true",
        help='Wrap query in quotes for exact phrase search (e.g. "a b" not a b)',
    )
    parser.add_argument(
        "--tee",
        action="store_true",
        help="With --clipboard, also print to stdout",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=importlib.metadata.version("strongshrew"),
    )
    args = parser.parse_args()

    output = generate(" ".join(args.query), exact=args.exact)

    if not args.clipboard or args.tee:
        sys.stdout.write(output)

    if args.clipboard:
        import pyperclip  # type: ignore[import-untyped]

        pyperclip.copy(output)


if __name__ == "__main__":
    main()
