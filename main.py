"""compiler_eea1e4 - File utility."""
import os, sys
from pathlib import Path
APP_TAG = "compiler_eea1e4"
def scan_directory(path: str = ".") -> list:
    entries = []
    for entry in Path(path).iterdir():
        if not entry.name.startswith("."):
            entries.append({"name": entry.name, "is_dir": entry.is_dir(), "size": entry.stat().st_size if entry.is_file() else 0})
    return sorted(entries, key=lambda x: x["name"])
def report(entries: list):
    print(f"[{APP_TAG}] Found {len(entries)} entries:")
    for e in entries[:10]:
        kind = "DIR " if e["is_dir"] else "FILE"
        print(f"  [{kind}] {e['name']} ({e['size']}B)")
def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    entries = scan_directory(target)
    report(entries)
if __name__ == "__main__":
    main()
