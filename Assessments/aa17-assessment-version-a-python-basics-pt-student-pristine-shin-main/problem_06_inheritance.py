# INHERITANCE
#
# Define two classes in this file.
#
# The "Light" class must have no constructor. It can be an empty class.
#
# The "LED" class should inherit from the "Light" class. It should have
# an empty constructor. It can be an empty class.

# WRITE YOUR CODE HERE
# Your code here
class Light:
  def my_method(self):
    print("Hello from the Light class.")

class LED(Light):
  def __init__(self):
    super().__init__()
  def my_method(self):
    print("Hello from the LED child class.")
