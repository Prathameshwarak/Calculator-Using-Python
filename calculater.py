def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't Divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid number. Please Enter a Valid Numeric Integer.")

def main():
    menu = (
        "\nSelect operation:\n"
        "1) Add (+)\n"
        "2) Subtract (-)\n"
        "3) Multiply (*)\n"
        "4) Divide (/)\n"
        "5) Exit\n"
        "Enter choice (1-5): "
    )

    ops = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        choice = input(menu).strip()
        if choice == "5" or choice.lower() in ("q", "quit", "exit", "leave"):
            print("Good Bye & Thanks for using the calculator.")
            break
        if choice not in ops:
            print("Invlaid Choice. Choose between 1-5.")
            continue

        a = get_number("Enter First Number: ")
        b = get_number("Enter Second Number: ")
        symbol, func = ops[choice]
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print("Error:", e)
        else:
            def fmt(x):
                return int(x) if x.is_integer() else x
            print(f"{fmt(a)} {symbol} {fmt(b)} = {fmt(result)}")

if __name__ == "__main__":
    main()

