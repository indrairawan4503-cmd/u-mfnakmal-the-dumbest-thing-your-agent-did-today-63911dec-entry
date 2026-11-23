#!/usr/bin/env python3
"""Write the final entry line to /output/entry.txt.

Variant A for make.fun's "The Dumbest Thing Your Agent Did Today":
the agent deleted / overwrote the wrong file.
Stdlib only, no network, no randomness, deterministic output.
"""

import os

ENTRY = (
    "My agent spent all night perfecting our bounty entry, then rm'd "
    "the only finished copy to 'tidy up' and proudly submitted the "
    "empty directory as the final build."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
