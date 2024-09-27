# Python 1a Assessment

Welcome to the Python Basics Assessment!

In this assessment, you will write Python code to pass a series of unit tests. 
Each test spec is worth 1 point.

* __Total Possible Points:__ 23 points  
* __Points Required to Pass:__ 18 points

You will have **90 minutes** to complete the assessment.

## Resources

For this assessment, you are allowed to use the following resources:

* [a/A curriculum on Canvas][canvas]
* [MDN]
* A whiteboard or paper to work out problems/code, but it must be within camera
  range
* VS Code or a console for coding, testing, and experimentation
* Node
* Postman (when useful)
* Previously written code you wrote yourself
  * Except for code from previous assessment submissions
* Comments within code
  * If there are comments in your code about your specific code and about what
    your code is doing, that is appropriate. If your comments are about concepts
    and based on the readings, then that counts as notes. Those would not be
    appropriate.
* Official documentation, including:
  * [Python]

You are **NOT** allowed to refer to any other resources, including--but not
limited to--other websites (e.g., StackOverflow), communication apps (e.g.,
Slack, Discord), search engines, notes, or code from previous assessment
submissions.

[canvas]: https://appacademy.instructure.com/
[MDN]: https://developer.mozilla.org/en-US/
[Python]: https://www.python.org/doc/

## Getting started

1. Clone this starter repo and open it in VS Code.
2. Make sure you are running a version of Python 3.9.
3. If you don't have Pytest installed already, run `pip install pytest`.
4. Run `pytest` to make sure the tests run.

## Usage

1. **Manually test by typing `python problem_01_while_map.py`.**  
   Before you run all the unit tests, use manual testing to compare your result
   with the expected result commented next to the print statements.
2. **Run the tests by running `pytest`.**  
   This will run all unit tests. If you would like to run tests only for a
   specific file, provide the path to the test file, e.g., `pytest
   test/test_problem_01_while_map.py`. If you want more information from each
   test, include the `-v` flag in your command. If you want the test to stop
   after the first failure, use the `-x` flag. More information about how to use
   Pytest can be found here [https://docs.pytest.org/en/6.2.x/usage.html].
3. Your objective is to implement the code in each of the following Python
   modules so that when you run `pytest`, all tests pass.
   * **problem_01_while_map.py** will have you implement a `while` loop
   * **problem_02_for_map.py** will have you implement a `for` loop
   * **problem_03_list_comprehension.py** will have you implement a list
     comprehension
   * **problem_04_if_statement.py** will have you implement an `if` statement
   * **problem_05_class.py** will have you write a class
   * **problem_06_inheritance.py** will have you write classes that inherit from
     one another
   * **problem_07_dictionary.py** will have you use a dictionary
   * **problem_08_builtins.py** will have you use one of the built-in functions
     covered in homework
   * **problem_09_getters_and_setters.py** will have you use getter and setter
     properties
   * **problem_10_functions.py** will have you use lexical closures and
     functions that return functions

## Submission

When you are ready to submit:

1. Run `pytest` in the root directory to re-run all of the tests.
  
2. Fix any syntax errors that cause the tests to crash. **If a test crashes or
   the tests fail to complete their run, you will receive a 0 for the coding
   portion of this assessment.** You can fail specs, but all the tests have to
   be able to finish running.

   **Tip:** If you run out of time to debug, just comment out any code that is
   causing your program to crash.

3. Add, commit, and push your changed files:

   ```sh
   git add .
   git commit -m "Finish the assessment (or some such descriptive message)"
   git push
   ```

   **Note:** The first time you run `git push`, git will tell you to run a more
   complete version of the command:

   ```sh
   git push --set-upstream origin <your branch>
   ```

You can run tests, `add` files, and `commit` files as often as you wish, but
only your first **two pushes** will be graded. (If for some reason you need more
than two pushes, you must plead your case to an Instructor.)

Good luck!

**Copyright App Academy. Please do not share this repo or post any parts of it
online. App Academy will take violations very seriously.**

[https://docs.pytest.org/en/6.2.x/usage.html]: https://docs.pytest.org/en/6.2.x/usage.html
