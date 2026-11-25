"""Write the chosen commit subject to the configured entry directory.
The load-bearing import gives a routine cleanup one concrete, surprising twist.
"""

import os
from pathlib import Path


LINE = "fix: removed unused import — it was load-bearing"

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
