"""
explained.py — Python Intro (what Python is and why people use it)

Run this file:  python explained.py
Read from top to bottom; comments tell you what each part means.
"""

# Python is a programming language you write in plain text, usually in files ending in .py.
# A program is a list of instructions the computer follows.

print("=" * 50)
print("Welcome — this line uses print() to show text on the screen.")
print("=" * 50)

# Python 3 is the current version family you should learn (Python 2 is retired).
# You can use Python for websites, automation, data work, games, and more.

topics = [
    "Readable syntax — often fewer lines than lower-level languages.",
    "Runs on Windows, macOS, and Linux.",
    "Huge standard library and many community packages.",
]

# --- Printing a numbered list from the `topics` list (loop + enumerate) ---
# "\n" at the start of the string = go to a new line before this heading so it is not glued to text above.
print("\nWhy people choose Python (examples):")

# `for ... in ...` runs the indented block once for each item we get from the right-hand side.
# `enumerate(topics, start=1)` does two things at once:
#   1) It walks through `topics` in order (first string, then second, then third).
#   2) It pairs each item with an index (a counter). With start=1, the first pair is (1, first_item),
#      the second is (2, second_item), etc. If we omitted start=1, counting would begin at 0 like most indexes in Python.
# Each time through the loop, Python unpacks one pair into two variable names: `i` (the number) and `line` (the text).
for i, line in enumerate(topics, start=1):
    # f-string: an f before the quotes lets you put expressions inside { ... }.
    # Here we print two spaces for indentation, then the number, a dot and space, then the string for this row.
    print(f"  {i}. {line}")

# This file is only a tiny demo. Your next folder (0.2_Get Started) shows how to run real code.
print("\nTip: open README in this folder for more detail, then continue the course order.")
