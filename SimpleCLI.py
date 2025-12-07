#!/usr/bin/env python3
"""
SimpleCLI – Level 1 function teaching tool

This script walks a beginner through the 4-part model of a Python function:
1) name (def line)
2) docstring
3) body
4) return
"""

import keyword

INDENT = " " * 4          # 4 real spaces
BAR = "|"                 # visual left border for CLI
VISIBLE_INDENT = "·" * 4  # 4 dots to show spaces


def ask_function_name() -> str:
    """
    Ask the user for a function name and validate it.

    If the name is empty or invalid, fall back to 'level1_message'.
    """
    print("Give your function a name (e.g., 'level1_message'):")
    raw = input("> ").strip()

    if not raw:
        print("\nNo name given. I will use 'level1_message'.\n")
        return "level1_message"

    if not raw.isidentifier() or keyword.iskeyword(raw):
        print(f"\n'{raw}' is not a valid Python function name.")
        print("I will use 'level1_message' instead.\n")
        return "level1_message"

    print(f"\nGreat, we will use '{raw}' as the function name.\n")
    return raw


def show_header() -> None:
    print("========================================")
    print(" Level 1 – Your first Python function")
    print(" 4-part model: name, docstring, body, return")
    print("========================================\n")


def main() -> None:
    show_header()

    func_name = ask_function_name()

    # Step 1: def line
    input("Step 1/4 – Press ENTER to see the function name line...")

    print("\n1) Function name (def line)")
    print("--------------------------------")
    print(f"def {func_name}():\n")
    print("- 'def' tells Python: I am defining a function.")
    print(f"- '{func_name}' is the function's name.")
    print("- '()' means: right now this function takes no inputs.\n")

    # Step 2: docstring
    input("Step 2/4 – Press ENTER to see the docstring...")

    print("\n2) Docstring (description for humans)")
    print("----------------------------------------")
    print(f"{INDENT}\"\"\"Say a simple message.\"\"\"\n")
    print("- A docstring is a short text that explains")
    print("  what the function does.")
    print("- It is the first line *inside* the function.")
    print("- NOTICE: it is indented with 4 spaces.\n")

    # Step 3: body
    input("Step 3/4 – Press ENTER to see the body (work part)...")

    print("\n3) Body (the work the function does)")
    print("-------------------------------------")
    print("\nHere is how the line REALLY looks in Python code:\n")
    print(f"{INDENT}message = \"Hello from a function\"\n")

    print("To make the indentation visible in the CLI, we draw a left border:\n")
    print(f"{BAR}{INDENT}message = \"Hello from a function\"")
    print(f"{BAR}{' ' * 4}^^^^")
    print(f"{BAR}These 4 spaces are the INDENT.\n")

    print("Same idea with dots instead of spaces:\n")
    print(f"{VISIBLE_INDENT}message = \"Hello from a function\"")
    print(f"{VISIBLE_INDENT}^^^^ = 4 spaces (indentation)\n")

    print("Explanation:")
    print("- The code line starts with 4 spaces (indentation).")
    print("- Then comes: message = \"Hello from a function\".")
    print("- In a real .py file you do NOT draw the '|' line or dots –")
    print("  they are only here to help you SEE the indentation.\n")

    # Step 4: return
    input("Step 4/4 – Press ENTER to see the return...")

    print("\n4) Return (send the result back)")
    print("---------------------------------")
    print(f"{INDENT}return message\n")
    print("- 'return' sends the result OUT of the function.")
    print("- Whatever you return can be used by the caller.")
    print("- This line is also indented with 4 spaces.\n")

    # Final step: show full function and call
    input("Last step – Press ENTER to CALL the function and see everything together...")

    print("\nNow we CALL the function and print its result.")
    print("Here is the full function code you could write in a .py file:\n")

    print("```python")
    print(f"def {func_name}():")
    print(f"{INDENT}\"\"\"Say a simple message.\"\"\"")
    print(f"{INDENT}message = \"Hello from a function\"")
    print(f"{INDENT}return message")
    print()
    print(f"print({func_name}())")
    print("```")
    print("\nIf you run that file, the output would be:\n")
    print("Output:")
    print("--------")
    print("Hello from a function\n")

    print("You have just seen a complete function:")
    print("- name")
    print("- docstring")
    print("- body")
    print("- return")
    print(f"And then we called it with print({func_name}()).")
    print("\nEnd of Level 1. 🎉")


if __name__ == "__main__":
    main()
