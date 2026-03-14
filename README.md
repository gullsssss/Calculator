# First project for portfolio in python

"Python" (https://img.shields.io/badge/Python-3.x-blue)
"Status" (https://img.shields.io/badge/status-active-success)
"License" (https://img.shields.io/badge/license-MIT-green)

A simple command-line calculator written in Python.
This program allows the user to perform basic mathematical operations by entering numbers and selecting an operation.

---

📌 Features

✔ Addition
✔ Subtraction
✔ Multiplication
✔ Division
✔ Power (exponentiation)
✔ Simple and beginner-friendly code
✔ Works in any terminal

---

📷 Example

Enter first number: 10
Enter operation (+, -, *, /, **): *
Enter second number: 5

Result: 50

---

⚙️ Requirements

- Python 3.x
- Any operating system (Windows, Linux, macOS)

Check Python version:

python --version

---

🚀 Installation

Clone this repository:

git clone https://github.com/your-username/calculator.git

Go to the project folder:

cd calculator

---

▶️ Usage

Run the program:

python calculator.py

Follow the instructions in the terminal:

1. Enter the first number
2. Enter the operation
3. Enter the second number
4. See the result

---

💻 Example Code

print("Calculator started")

a = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /, **): ")
b = float(input("Enter second number: "))

if operation == "+":
    result = a + b

elif operation == "-":
    result = a - b

elif operation == "*":
    result = a * b

elif operation == "/":
    result = a / b

elif operation == "**":
    result = a ** b

else:
    print("Unknown operation")
    result = None

if result is not None:
    print("Result:", result)

---

📂 Project Structure

calculator/
│
├── calculator.py
└── README.md

---

🧠 How It Works

The program:

1. Asks the user to input numbers.
2. Asks for the mathematical operation.
3. Uses "if / elif" conditions to determine which operation to perform.
4. Prints the result.

---

🛠 Future Improvements

Possible improvements:

- Add graphical interface (GUI)
- Add calculation history
- Add more mathematical operations
- Handle errors (division by zero)

---

🤝 Contributing

Contributions are welcome.

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project.

---

⭐ If you like this project, consider giving it a star on GitHub!
