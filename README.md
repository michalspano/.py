# .py --- A Python Repositery

This repositery contains programs, projects and much more for suitable for any
__Python enthusiast.__

## About Python
Python is a high-level programming language used for general-purpose software engineering. It’s a server side language – which means it runs on the server, and is responsible for processing the logic behind user inputs, interacting with databases and other servers, etc.

Initially developed in the late 1980’s by Guido Van Rossum, Python has been around for decades alongside other server side languages like Java and C. Van Rossum modeled Python after the English language, eliminating unnecessary syntax to make it easier to read and write than other programming languages.

Python is an open-sourced language, and in recent years has increased in popularity due to its use in data science. Python also has a strong community around machine learning, data modeling, data analysis and artificial intelligence (AI), with extensive resources and libraries built for these purposes.

And yes, the rumors are true. Python is named after the British comedy group Monty Python. Which in our opinion makes it all the more awesome. [[1]][WIKI]

## Why Learn Python?

Just to name a few of its most common uses, Python is used in Data Mining, Data Science, AI, Machine Learning, Web Development, Web Frameworks, Embedded Systems, Graphic Design applications, Gaming, Network development, Product development, Rapid Application Development, Testing, Automation Scripting, the list goes on.

Python is used as an easier and more efficiently-written alternative to languages that perform similar functionalities like C, R, and Java. Therefore Python is growing in popularity as the primary language for many applications.

On average, a Python developer earns $119,082 per year in the US. Additionally, the average salaries from 2017 to 2020 show that Python ranks consistently within the top 3 highest paying languages. [[2]][WIKI]
## Execution
### macOS / Linux

```shell
$ python3 $INPUT_FILE
```

### Windows
```shell
$ python $INPUT_FILE
```

`$INPUT_FILE` represents the local path of the desired `.py` file.

## Highlights
### Python - Shell Script Integration

```python
# Integrate Python with Shell script
import os


# Create the main function
def main():
    # Get the path of the shell script
    shell_path = input("Input path of the script: ")
    # Execute the shell script

    """
    Using 'os.system' to work as a bash command line 'sh' to execute a .sh file.
    Possible alternatives: 
    ./shell_path
    chmod +x shell_path
    ... 
    """

    execute_command(shell_path)


# Define a command executor function
def execute_command(path: str):
    os.system(f"sh {path}")
    """
    Possibly pass in the .sh path as a command line argument using:
    'from sys import argv'
    And iterate the argument vector.
    """


if __name__ == '__main__':
    main()

```

Default `.sh` script.

```shell
#!/bin/bash

# This is a sample shell program
function MAIN()
{
  # Prompt the user
  echo "Hello from Shell script!"
}

# Call the main function
MAIN

```

### Box Blur Filter
```python
# Define main function
def main(*argv):

    # Using Pillow (PIL)
    from PIL import Image
    from PIL import ImageFilter

    # Proceed to the effect (box blur)
    input_file = Image.open(argv[0], "r")
    output_file = input_file.filter(ImageFilter.BoxBlur(argv[2]))
    output_file.save(argv[1])


# Define maine executable pathway
if __name__ == "__main__":

    # Define variables to be passed to the main function
    inputPath: str = input("Input PATH: ")
    outputPath: str = input("Output PATH: ")
    ratio: int = int(input("Filter ratio: "))

    #  Call the main function
    main(inputPath, outputPath, ratio)

```

<!-- LINKS AND REFS -->
[WIKI]: https://codingnomads.co/why-learn-python/