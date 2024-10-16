import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    error = False
    i = 0
    line = 1  # Initialize the line counter
    while i < len(file_contents):
        c = file_contents[i]

        if c == "\n":
            line += 1  # Increment line number on newlines
        elif c == "(":
            print(f"LEFT_PAREN ( null at line {line}")
        elif c == "{":
            print(f"LEFT_BRACE {{ null at line {line}")
        elif c == "*":
            print(f"STAR * null at line {line}")
        elif c == ".":
            print(f"DOT . null at line {line}")
        elif c == ",":
            print(f"COMMA , null at line {line}")
        elif c == "+":
            print(f"PLUS + null at line {line}")
        elif c == "-":
            print(f"MINUS - null at line {line}")
        elif c == ";":
            print(f"SEMICOLON ; null at line {line}")
        elif c == "}":
            print(f"RIGHT_BRACE }} null at line {line}")
        elif c == ")":
            print(f"RIGHT_PAREN ) null at line {line}")
        elif c == "=":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print(f"EQUAL_EQUAL == null at line {line}")
                i += 1  # Skip the next character since it's part of '=='
            else:
                print(f"EQUAL = null at line {line}")
        elif c == "!":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print(f"BANG_EQUAL != null at line {line}")
                i += 1  # Skip the next character since it's part of '!='
            else:
                print(f"BANG ! null at line {line}")
        elif c == "<":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print(f"LESS_EQUAL <= null at line {line}")
                i += 1  # Skip the next character since it's part of '<='
            else:
                print(f"LESS < null at line {line}")
        elif c == ">":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print(f"GREATER_EQUAL >= null at line {line}")
                i += 1  # Skip the next character since it's part of '>='
            else:
                print(f"GREATER > null at line {line}")
        elif c == "/":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "/":
                i += 1  # Skip the next character since it's part of '//'
                # Skip comments until the end of the line
                while i < len(file_contents) and file_contents[i] != "\n":
                    i += 1
            else:
                print(f"SLASH / null at line {line}")
        elif c == " " or c == "\r" or c == "\t":
            # Ignore spaces, carriage returns, and tabs
            pass
        else:
            error = True
            print(f"[line {line}] Error: Unexpected character: {c}", file=sys.stderr)

        i += 1  # Move to the next character after processing the current one

    print("EOF null")
    if error:
        exit(65)  # Exit with an error code if any error occurred
    else:
        exit(0)  # Exit normally if no errors occurred

if __name__ == "__main__":
    main()
