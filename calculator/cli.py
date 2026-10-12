from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


OPERATIONS = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}


def main():
    history = []
    print("Calculator ready! Type help for commands.")

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("Goodbye!")
            break

        if not user_input:
            continue

        parts = user_input.split()
        name = parts[0].lower()

        if name == "exit":
            print("Goodbye!")
            break

        if name == "help":
            print("Commands: add, subtract, multiply, divide, history, exit")
            continue

        if name == "history":
            entries = HistoryCommand(history).execute()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("History is empty.")
            continue

        if name not in OPERATIONS:
            print("Unknown command. Type help.")
            continue

        if len(parts) != 3:
            print("Please enter exactly two numbers.")
            continue

        try:
            a = float(parts[1])
            b = float(parts[2])

            # Input -> strategy -> factory -> command -> result.
            operation = OPERATIONS[name]
            calculation = ArithmeticCalculation.create(a, b, operation)
            command = CalculateCommand(calculation, history)
            print(f"{command.execute():g}")

        except ValueError as error:
            print(f"Error: {error}")
