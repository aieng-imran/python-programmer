# Define a minimal class with an attribute
class MyClass:
    """A minimal example class
    
    :param value: value to set as the ``attribute`` attribute
    :ivar attribute: contains the contents of ``value`` passed in init
    """
# Method to create a new instance of MyClass
    def __init__(self, value, name):
# Define attribute with the contents of the value param
        self.attribute = value
        self.name = name
    
    def name(self):
        print(self.name)