
from pathlib import Path

files = ["Add.hack", "Max.hack", "Rect.hack", "Pong.hack"]

for filename in files:
    path = Path("test_files") / filename

    print(f"\nChecking {filename}...")

    if not path.exists():
        print("FILE NOT FOUND")
        continue

    lines = path.read_text().splitlines()

    invalid = [
        (i + 1, line)
        for i, line in enumerate(lines)
        if len(line) != 16 or any(bit not in "01" for bit in line)
    ]

    if not lines:
        print("FAIL: Empty file")
    elif invalid:
        print("FAIL: Invalid machine code")
        print(invalid[:5])
    else:
        print("PASS: All instructions are valid 16-bit binary")

    print("Total instructions:", len(lines))
