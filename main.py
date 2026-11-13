from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(exist_ok=True)

joke = "I asked my coding agent to fix a typo; it refactored 47 files, and now the typo runs its own sprint."
(output_dir / "entry.txt").write_text(joke, encoding="utf-8")
