import sys

RESERVED_WORDS = {
    "and", "class", "else", "false", "for", "fun", 
    "if", "nil", "or", "print", "return", "super", 
    "this", "true", "var", "while"
}

def main():
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh <tokenize|parse> <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command not in ["tokenize", "parse"]:
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()
        
    if command == "tokenize":
        tokenize(file_contents)
    elif command == "parse":
        parse(file_contents)

def tokenize(file_contents):
    error = False
    i = 0
    line = 1

    while i < len(file_contents):
        c = file_contents[i]

        if c == "\n":
            line += 1
        elif c == "(":
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
                i += 1
            else:
                print("EQUAL = null")
        elif c == "!":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("BANG_EQUAL != null")
                i += 1
            else:
                print("BANG ! null")
        elif c == "<":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("LESS_EQUAL <= null")
                i += 1
            else:
                print("LESS < null")
        elif c == ">":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("GREATER_EQUAL >= null")
                i += 1
            else:
                print("GREATER > null")
        elif c == "/":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "/":
                i += 2
                while i < len(file_contents) and file_contents[i] != "\n":
                    i += 1
                line += 1
            else:
                print("SLASH / null")
        elif c in " \r\t":
            pass
        elif c == '"':
            word = ""
            i += 1
            while i < len(file_contents) and file_contents[i] != '"':
                word += file_contents[i]
                i += 1
            if i == len(file_contents):
                error = True
                print(f"[line {line}] Error: Unterminated string.", file=sys.stderr)
            else:
                print(f'STRING "{word}" {word}')
        elif c.isdigit():
            start = i
            has_dot = False
            while i < len(file_contents) and (file_contents[i].isdigit() or file_contents[i] == "."):
                if file_contents[i] == ".":
                    if has_dot:
                        error = True
                        print(f"[line {line}] Error: Unexpected character: .", file=sys.stderr)
                        break
                    has_dot = True
                i += 1
            number = file_contents[start:i]
            try:
                float_value = float(number)
                if float_value.is_integer():
                    normalized_value = f"{int(float_value)}.0"
                else:
                    normalized_value = f"{float_value:.2f}"
                print(f"NUMBER {number} {normalized_value}")
            except ValueError:
                error = True
                print(f"[line {line}] Error: Invalid number literal: {number}", file=sys.stderr)
            continue
        elif c.isalpha() or c == "_":
            start = i
            while i < len(file_contents) and (file_contents[i].isalnum() or file_contents[i] == "_"):
                i += 1
            identifier = file_contents[start:i]
            if identifier in RESERVED_WORDS:
                print(f"{identifier.upper()} {identifier} null")
            else:
                print(f"IDENTIFIER {identifier} null")
            continue
        else:
            error = True
            print(f"[line {line}] Error: Unexpected character: {c}", file=sys.stderr)
        i += 1

    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)

def parse(file_contents):
    tokens = []
    i = 0
    line = 1
    error = False

    while i < len(file_contents):
        c = file_contents[i]

        if c == "\n":
            line += 1
        elif c in " \r\t":
            pass
        elif c.isdigit():
            start = i
            has_dot = False
            while i < len(file_contents) and (file_contents[i].isdigit() or file_contents[i] == "."):
                if file_contents[i] == ".":
                    if has_dot:
                        error = True
                        print(f"[line {line}] Error: Unexpected character: .", file=sys.stderr)
                        break
                    has_dot = True
                i += 1
            number = file_contents[start:i]
            try:
                float_value = float(number)
                if float_value.is_integer():
                    normalized_value = f"{int(float_value)}.0"
                else:
                    normalized_value = f"{float_value:.2f}"
                tokens.append(normalized_value)
            except ValueError:
                error = True
                print(f"[line {line}] Error: Invalid number literal: {number}", file=sys.stderr)
                break
            continue
        elif c == '"':
            word = ""
            i += 1
            while i < len(file_contents) and file_contents[i] != '"':
                word += file_contents[i]
                i += 1
            if i == len(file_contents):
                error = True
                print(f"[line {line}] Error: Unterminated string literal.", file=sys.stderr)
                break
            tokens.append(word)
        elif c == "+":
            tokens.append("+")
        elif c == "-":
            tokens.append("-")
        elif c == "(":
            tokens.append("(")
        elif c == ")":
            tokens.append(")")
        elif c.isalpha() or c == "_":
            start = i
            while i < len(file_contents) and (file_contents[i].isalnum() or file_contents[i] == "_"):
                i += 1
            identifier = file_contents[start:i]
            tokens.append(identifier)
            continue
        else:
            error = True
            print(f"[line {line}] Error: Unexpected character: {c}", file=sys.stderr)
            break
        i += 1

    if not error:
        ast = parse_expression(tokens)
        if ast:
            print(f'"{ast}"')
        else:
            print("Error: Invalid expression.")

    if error:
        exit(65)
    else:
        exit(0)

def parse_expression(tokens):
    if len(tokens) == 0:
        return None
    token = tokens.pop(0)

    if token == "(":
        expr = parse_expression(tokens)
        if expr is not None and len(tokens) > 0 and tokens[0] == ")":
            tokens.pop(0)
            return f"(group {expr}"
        else:
            return "Error: Mismatched parentheses."
    else:
        left = token
        if len(tokens) == 0:
            return left
        operator = tokens.pop(0)
        if len(tokens) == 0:
            return None
        right = tokens.pop(0)
        return f"({operator} {left} {right})"

if __name__ == "__main__":
    main()
