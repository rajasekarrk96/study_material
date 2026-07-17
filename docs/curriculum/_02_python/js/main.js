// Sample data for our Python learning content
const contentData = {
    introduction: {
        title: "Introduction to Python",
        description: `
            <p>Python is a high-level, interpreted programming language known for its simplicity and readability. 
            Created by Guido van Rossum and first released in 1991, Python has become one of the most popular 
            programming languages in the world.</p>
            
            <h2>Why Learn Python?</h2>
            <ul>
                <li>Easy to learn and read</li>
                <li>Versatile (Web development, Data Science, AI, Automation, etc.)</li>
                <li>Large standard library</li>
                <li>Strong community support</li>
                <li>Cross-platform compatibility</li>
            </ul>
            
            <h2>Python Installation</h2>
            <p>To get started with Python, you'll need to install it on your computer:</p>
            <ol>
                <li>Visit <a href="https://www.python.org/downloads/" target="_blank">python.org</a></li>
                <li>Download the latest version for your operating system</li>
                <li>Run the installer and make sure to check "Add Python to PATH"</li>
                <li>Verify installation by opening a terminal and typing: <code>python --version</code></li>
            </ol>
        `,
        example: `
            <h2>Your First Python Program</h2>
            <p>Let's write a simple "Hello, World!" program in Python:</p>
            <div class="code-block">
                <pre><code># This is a simple Python program
print("Hello, World!")  # This line prints text to the console</code></pre>
            </div>
            <p>To run this program:</p>
            <ol>
                <li>Open a text editor and type the code above</li>
                <li>Save the file with a <code>.py</code> extension (e.g., <code>hello.py</code>)</li>
                <li>Open a terminal, navigate to the file location, and run: <code>python hello.py</code></li>
            </ol>
        `,
        workout: [
            {
                question: "Write a Python program to print your name and age.",
                input: "# No input required",
                output: "John Doe, 25",
                answer: `
                    <div class="code-block">
                        <pre><code>name = "John Doe"
age = 25
print(f"{name}, {age}")</code></pre>
                    </div>
                    <p>This program demonstrates basic variable assignment and string formatting in Python.</p>
                `
            },
            {
                question: "Write a Python program to add two numbers and print the result.",
                input: "5, 7",
                output: "12",
                answer: `
                    <div class="code-block">
                        <pre><code># Adding two numbers
num1 = 5
num2 = 7

# Calculate sum
sum = num1 + num2

# Display the result
print(sum)  # Output: 12</code></pre>
                    </div>
                `
            }
        ]
    },
    basics: {
        title: "Python Basics",
        description: `
            <h2>Variables and Data Types</h2>
            <p>In Python, you don't need to declare variables before using them or declare their type. 
            The interpreter automatically determines the type of a variable based on the value assigned to it.</p>
            
            <h3>Basic Data Types</h3>
            <ul>
                <li><strong>Numbers:</strong> int, float, complex</li>
                <li><strong>Text:</strong> str (strings)</li>
                <li><strong>Boolean:</strong> bool (True/False)</li>
                <li><strong>Sequence Types:</strong> list, tuple, range</li>
                <li><strong>Mapping Type:</strong> dict</li>
                <li><strong>Set Types:</strong> set, frozenset</li>
                <li><strong>Binary Types:</strong> bytes, bytearray, memoryview</li>
            </ul>
            
            <h2>Basic Operators</h2>
            <p>Python supports various types of operators:</p>
            <ul>
                <li>Arithmetic Operators: +, -, *, /, %, **, //</li>
                <li>Comparison Operators: ==, !=, >, <, >=, <=</li>
                <li>Logical Operators: and, or, not</li>
                <li>Assignment Operators: =, +=, -=, *=, /=, etc.</li>
                <li>Identity Operators: is, is not</li>
                <li>Membership Operators: in, not in</li>
            </ul>
        `,
        example: `
            <h2>Working with Variables and Data Types</h2>
            <div class="code-block">
                <pre><code># Variables and Data Types
# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

# List
fruits = ["apple", "banana", "cherry"]

# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Print variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)
print("Favorite fruits:", fruits)
print("Person details:", person)</code></pre>
            </div>
            
            <h2>Basic Operations</h2>
            <div class="code-block">
                <pre><code># Basic arithmetic operations
a = 10
b = 3

print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division (returns float)
print("a // b =", a // b)  # Floor division (returns int)
print("a % b =", a % b)   # Modulus (remainder)
print("a ** b =", a ** b)  # Exponentiation

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print("Full name:", full_name)

# String methods
message = "hello, world!"
print(message.upper())      # HELLO, WORLD!
print(message.capitalize()) # Hello, world!
print(message.replace("world", "Python"))  # hello, Python!</code></pre>
            </div>
        `,
        workout: [
            {
                question: "Create variables to store your name, age, and favorite programming language. Then print them in a formatted string.",
                input: "No input required",
                output: "My name is Alice, I'm 25 years old, and my favorite programming language is Python.",
                answer: `
                    <div class="code-block">
                        <pre><code># Variables
name = "Alice"
age = 25
favorite_language = "Python"

# Formatted string using f-strings (Python 3.6+)
print(f"My name is {name}, I'm {age} years old, and my favorite programming language is {favorite_language}.")

# Alternative using .format() method (works in older Python versions)
# print("My name is {}, I'm {} years old, and my favorite programming language is {}.".format(name, age, favorite_language))</code></pre>
                    </div>
                `
            },
            {
                question: "Write a program that calculates the area of a rectangle. The length is 10 and width is 5.",
                input: "length = 10, width = 5",
                output: "The area of the rectangle is: 50",
                answer: `
                    <div class="code-block">
                        <pre><code># Calculate area of a rectangle
length = 10
width = 5

# Area = length * width
area = length * width

# Display the result
print("The area of the rectangle is:", area)

# Alternatively, using a function
def calculate_rectangle_area(length, width):
    return length * width

# Call the function
result = calculate_rectangle_area(10, 5)
print("The area of the rectangle is:", result)</code></pre>
                    </div>
                `
            }
        ]
    },
    conditions: {
        title: "Conditional Statements",
        description: `
            <h2>If, Elif, and Else Statements</h2>
            <p>Conditional statements in Python allow you to execute different blocks of code based on certain conditions.</p>
            
            <h3>if Statement</h3>
            <p>The <code>if</code> statement is used to test a specific condition. If the condition is true, the block of code inside the if statement will be executed.</p>
            
            <h3>elif Statement</h3>
            <p>The <code>elif</code> (short for "else if") allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.</p>
            
            <h3>else Statement</h3>
            <p>The <code>else</code> statement catches anything which isn't caught by the preceding conditions.</p>
            
            <h2>Comparison Operators</h2>
            <p>Comparison operators are used to compare values:</p>
            <ul>
                <li><code>==</code> Equal to</li>
                <li><code>!=</code> Not equal to</li>
                <li><code>></code> Greater than</li>
                <li><code><</code> Less than</li>
                <li><code>>=</code> Greater than or equal to</li>
                <li><code><=</code> Less than or equal to</li>
            </ul>
            
            <h2>Logical Operators</h2>
            <p>Logical operators are used to combine conditional statements:</p>
            <ul>
                <li><code>and</code> Returns True if both statements are true</li>
                <li><code>or</code> Returns True if one of the statements is true</li>
                <li><code>not</code> Reverse the result, returns False if the result is true</li>
            </ul>
        `,
        example: `
            <h2>If-Elif-Else Examples</h2>
            <div class="code-block">
                <pre><code># Simple if statement
age = 20
if age >= 18:
    print("You are an adult.")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not too hot today.")

# if-elif-else statement
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# Nested if statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")</code></pre>
            </div>
            
            <h2>Logical Operators in Conditions</h2>
            <div class="code-block">
                <pre><code># Using 'and' operator
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can rent a car.")
else:
    print("You cannot rent a car.")

# Using 'or' operator
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("It's time to relax!")
else:
    print("It's a working day.")

# Using 'not' operator
is_raining = False
if not is_raining:
    print("You don't need an umbrella.")
else:
    print("Better take an umbrella.")

# Combining multiple conditions
age = 22
has_ticket = True
has_id = True

if (age >= 18 and has_id) and has_ticket:
    print("You can enter the club.")
elif age >= 18 and has_id and not has_ticket:
    print("You need to buy a ticket first.")
else:
    print("You cannot enter the club.")</code></pre>
            </div>
        `,
        workout: [
            {
                question: "Write a program that checks if a number is positive, negative, or zero.",
                input: "5",
                output: "The number 5 is positive.",
                answer: `
                    <div class="code-block">
                        <pre><code># Check if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print("The number is zero.")</code></pre>
                    </div>
                `
            },
            {
                question: "Write a program that determines if a year is a leap year or not. A leap year is divisible by 4, but not by 100 unless it's also divisible by 400.",
                input: "2024",
                output: "2024 is a leap year.",
                answer: `
                    <div class="code-block">
                        <pre><code># Check if a year is a leap year
year = int(input("Enter a year: "))

# A year is a leap year if:
# 1. It's divisible by 4 but not by 100, or
# 2. It's divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")</code></pre>
                    </div>
                `
            }
        ]
    },
    loops: {
        title: "Loops in Python",
        description: `
            <h2>Loops in Python</h2>
            <p>Loops are used to repeatedly execute a block of code. Python provides two types of loops:</p>
            
            <h3>1. for Loop</h3>
            <p>The <code>for</code> loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).</p>
            
            <h3>2. while Loop</h3>
            <p>The <code>while</code> loop executes a set of statements as long as a condition is true.</p>
            
            <h2>Loop Control Statements</h2>
            <p>Python provides several statements to control the flow of loops:</p>
            <ul>
                <li><code>break</code> - Stops the loop before it has looped through all the items</li>
                <li><code>continue</code> - Skips the current iteration and continues with the next</li>
                <li><code>pass</code> - Does nothing, used as a placeholder</li>
                <li><code>else</code> - Specifies a block of code to be executed when the loop is finished</li>
            </ul>
            
            <h2>range() Function</h2>
            <p>The <code>range()</code> function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.</p>
            
            <h2>Enumerate Function</h2>
            <p>The <code>enumerate()</code> function takes a collection (e.g., a list) and returns it as an enumerate object. This function adds a counter as the key of the enumerate object.</p>
        `,
        example: `
            <h2>For Loop Examples</h2>
            <div class="code-block">
                <pre><code># Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}s")

# Using range()
print("Counting to 5:")
for i in range(1, 6):  # range(start, stop, step)
    print(i, end=" ")
print("\n")

# Looping through a string
message = "Python"
for char in message:
    print(char, end="-")
print("\n")

# Looping with index using enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Nested for loops
print("\nMultiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("--------")</code></pre>
            </div>
            
            <h2>While Loop Examples</h2>
            <div class="code-block">
                <pre><code># Basic while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Don't forget to increment the counter

# Using break and continue
print("\nBreak and Continue:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    if num > 7:
        break  # Exit loop when num > 7
    print(num)

# Using else with while
print("\nElse with while:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop completed!")

# Infinite loop with break
print("\nGuessing game:")
import random
secret_number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")</code></pre>
            </div>
        `,
        workout: [
            {
                question: "Write a program that prints the Fibonacci sequence up to n terms.",
                input: "8",
                output: "0, 1, 1, 2, 3, 5, 8, 13",
                answer: `
                    <div class="code-block">
                        <pre><code># Program to display the Fibonacci sequence up to n terms
n = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1, end=", ")
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1</code></pre>
                    </div>
                `
            },
            {
                question: "Write a program that prints the multiplication table for a given number up to 10.",
                input: "5",
                output: "5 x 1 = 5\n5 x 2 = 10\n...\n5 x 10 = 50",
                answer: `
                    <div class="code-block">
                        <pre><code># Multiplication table
number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Using while loop
print("\nUsing while loop:")
count = 1
while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1</code></pre>
                    </div>
                `
            }
        ]
    }
};

// DOM Elements
const navItems = document.querySelectorAll('.nav-item');
const contentArea = document.getElementById('content');
const progressBar = document.querySelector('.progress');
const progressPercent = document.querySelector('.progress-percent');

// Track completed sections
let completedSections = new Set();

// Initialize the page
function init() {
    // Load the first section by default
    loadContent('introduction');
    
    // Add click event listeners to navigation items
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const page = item.getAttribute('data-page');
            loadContent(page);
            
            // Update active state
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');
        });
    });
    
    // Update progress
    updateProgress();
}

// Load content based on page
function loadContent(page) {
    const content = contentData[page];
    if (!content) return;
    
    let workoutSection = '';
    if (content.workout && content.workout.length > 0) {
        workoutSection = `
            <div class="workout-sheet">
                <h3>Workout Sheet</h3>
                ${content.workout.map((item, index) => `
                    <div class="workout-question">
                        <h4>${index + 1}. ${item.question}</h4>
                        <p><strong>Input:</strong> ${item.input}</p>
                        <p><strong>Expected Output:</strong> ${item.output}</p>
                        <button class="show-answer" data-answer="answer-${page}-${index}">Show Answer</button>
                        <div id="answer-${page}-${index}" class="workout-answer">
                            ${item.answer}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    contentArea.innerHTML = `
        <div class="content-card">
            <h1>${content.title}</h1>
            <div class="content-description">
                ${content.description}
            </div>
            <div class="content-example">
                ${content.example || ''}
            </div>
            ${workoutSection}
            <div class="navigation-buttons">
                <button id="mark-complete" class="btn btn-primary">Mark as Completed</button>
            </div>
        </div>
    `;
    
    // Add event listeners to show/hide answers
    document.querySelectorAll('.show-answer').forEach(button => {
        button.addEventListener('click', function() {
            const answerId = this.getAttribute('data-answer');
            const answerElement = document.getElementById(answerId);
            
            if (answerElement.style.display === 'block') {
                answerElement.style.display = 'none';
                this.textContent = 'Show Answer';
            } else {
                answerElement.style.display = 'block';
                this.textContent = 'Hide Answer';
            }
        });
    });
    
    // Add event listener to mark as complete button
    const markCompleteBtn = document.getElementById('mark-complete');
    if (markCompleteBtn) {
        markCompleteBtn.addEventListener('click', () => {
            if (completedSections.has(page)) {
                completedSections.delete(page);
                markCompleteBtn.textContent = 'Mark as Completed';
                markCompleteBtn.classList.remove('completed');
            } else {
                completedSections.add(page);
                markCompleteBtn.textContent = 'Completed ✓';
                markCompleteBtn.classList.add('completed');
            }
            updateProgress();
        });
        
        // Update button state if section is already completed
        if (completedSections.has(page)) {
            markCompleteBtn.textContent = 'Completed ✓';
            markCompleteBtn.classList.add('completed');
        }
    }
}

// Update progress bar
function updateProgress() {
    const totalSections = Object.keys(contentData).length;
    const completedCount = completedSections.size;
    const percent = Math.round((completedCount / totalSections) * 100);
    
    progressBar.style.width = `${percent}%`;
    progressPercent.textContent = `${percent}%`;
}

// Initialize the application when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);
