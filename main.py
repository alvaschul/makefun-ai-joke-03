import os

JOKE_PARTS = [
    "I asked my coding agent to fix a typo; ",
    "it refactored 47 files, and now the typo runs its own sprint.",
]


def build_output():
    os.makedirs("/output", exist_ok=True)
    target = os.path.join("/output", "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write("".join(JOKE_PARTS))


if __name__ == "__main__":
    build_output()
