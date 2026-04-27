import sys


def main() -> None:
    if sys.stdin.isatty():
        name = input("Your name: ")
        print("Hello,", name)
    else:
        # Non-interactive run (e.g. piped input): use a default
        print("No TTY; skipping input demo. Run in terminal for input().")


if __name__ == "__main__":
    main()
