"""A simple command-line calculator."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    """Run a calculator operation by name."""
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    try:
        selected_operation = operations[operation.lower()]
    except KeyError as exc:
        raise ValueError(f"Unknown operation: {operation}") from exc

    return selected_operation(a, b)


def main() -> None:
    """Run the calculator with a simple REPL pattern."""
    print("Python Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.")

    while True:
        operation = input("\nOperation: ").strip().lower()
        if operation in {"quit", "exit"}:
            print("Goodbye!")
            break

        try:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))
            result = calculate(operation, first_number, second_number)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":  # pragma: no cover
    main()