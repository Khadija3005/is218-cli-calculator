# IS218 CLI Calculator

This project is a Python calculator that uses object-oriented programming, design patterns, and automated testing.

## Setup

Requires Python 3.12 or newer.

1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install requirements: `python -m pip install -r requirements.txt`

## Run

Run the calculator with:

`python -m calculator`

Example:

- `add 5 3` gives 8
- `subtract 5 3` gives 2
- `multiply 5 3` gives 15
- `divide 6 3` gives 2
- `history` shows successful calculations
- `exit` closes the calculator

## Testing

Run:

`python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100`

The project has 20 passing tests and 100% line coverage locally.

## OOP Concepts

- Encapsulation: Calculation stores its numbers and operation. HistoryCommand protects the history list by returning a copy.
- Abstraction: Calculation is an abstract class that requires execute().
- Inheritance: ArithmeticCalculation inherits from Calculation.
- Polymorphism: Different calculation implementations can use execute().
- Composition: CalculateCommand contains a calculation, and a calculation contains an operation.

## SOLID Principles

- Single Responsibility: Each class has one main job.
- Open/Closed: New operations can be added without changing calculation execution or command execution.
- Liskov Substitution: A calculation implementation must return a numeric result or raise an appropriate error.
- Interface Segregation: Calculation only requires execute().
- Dependency Inversion: CalculateCommand depends on the Calculation abstraction instead of a specific operation.

## Method Types

- Static: Operations.add() performs math without object state.
- Class: create() builds a calculation object using cls.
- Instance: execute() uses the object's stored values.

## Design Patterns

- Factory: ArithmeticCalculation.create() creates calculation objects.
- Command: CalculateCommand runs calculations and saves successful results. HistoryCommand retrieves history.
- Strategy: The CLI selects arithmetic operations from a dictionary.

Subtraction, multiplication, and division were added after addition. The calculation execution code does not need to change because it uses the selected operation.

## Coverage Exclusions

The abstract execute() placeholder is excluded because it has no implementation. The entry point in __main__.py is excluded because it only starts the tested CLI.

## GitHub Actions

Successful run: https://github.com/Khadija3005/is218-cli-calculator/actions/runs/38278234344
