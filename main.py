"""Make.fun entry: Sum up 25 November's world news in one image.

Writes the bundled image to /output/entry.png (ENTRY_OUTPUT override
for local testing). No network, deterministic: the same bytes every run.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
    try:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        shutil.copyfile(SRC, output_path)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output", "entry.png")
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        shutil.copyfile(SRC, fallback)


if __name__ == "__main__":
    main()
