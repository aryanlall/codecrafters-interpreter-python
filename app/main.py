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
    while i < len(file_contents):
        c = file_contents[i]
        if c == "(":
            print("LEFT_PAREN ( null")
        elif c == "{":
            print("LEFT_BRACE { null")
        elif c == "*":
            print("STAR * null")
        elif c == ".":
            print("DOT . null")
        elif c == ",":
            print("COMMA , null")
        elif c == "+":
            print("PLUS + null")
        elif c == "-":
            print("MINUS - null")
        elif c == ";":
            print("SEMICOLON ; null")
        elif c == "}":
            print("RIGHT_BRACE } null")
        elif c == ")":
            print("RIGHT_PAREN ) null")
        elif c == "=":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("EQUAL_EQUAL == null")
                i+=1
            else:
                print("EQUAL = null")
        elif c == "!":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("BANG_EQUAL != null")
                i+=1
            else:
                print("BANG ! null")
        elif c == "<":
            print("LESS_EQUAL < null")
        elif c == ">":
            print("GREAT_EQUAL > null")
        else:
            error = True
            line_number = file_contents.count("\n", 0, file_contents.find(c)) + 1
            print("[line %s] Error: Unexpected character: %s" % (line_number, c), file=sys.stderr,)
        i+=1
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
