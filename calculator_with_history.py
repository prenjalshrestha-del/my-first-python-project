HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No history found.")
        return

    if len(lines) == 0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())


def clear_history():
    with open(HISTORY_FILE, "w"):
        pass
    print("History cleared.")


def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + " = " + str(result) + "\n")


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number")
        return

    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
        return

    op = parts[1]

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    display_result = int(result) if result.is_integer() else result
    print("Result:", display_result)
    save_to_history(user_input, display_result)


def main():
    print('---SIMPLE CALCULATOR WITH HISTORY---')
    while True:
        raw_input = input("Enter an equation (e.g., 2 + 2) or type 'history' to view history, 'clear' to clear history, or 'exit' to quit: ").strip()
        command = raw_input.lower()

        if command == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif command == "clear":
            clear_history()
        elif command == "history":
            show_history()
        else:
            calculate(raw_input)


if __name__ == "__main__":
    main()
