# link : https://www.pythontutorial.net/python-oop/python-instance-variables/

from pprint import pprint


# Introduction to the instance variables


# A Class with two variables
class HtmlDocument:
    version = 5
    extension = "HTML"


pprint(HtmlDocument.__dict__)

# [Output]
# mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
#               '__doc__': None,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
#               'extension': 'HTML',
#               'version': 5})

print(HtmlDocument.version)
# [Output] 5
print(HtmlDocument.extension)
# [Output] HTML

"""
The 'HtmlDocument' class has two class variables:
- 'extension'
- 'version'
Python will stores these two class variables in the
'__dict__' attribute.

When you access the class variables via the class,
Python looks them up in the '__dict__' of the class.
"""


# Creates a new instance of the 'HtmlDocument' class.
home = HtmlDocument()

"""
- The 'home' is an instance of the 'HtmlDocument' class.
- The 'home' instance has its own '__dict__' attribute.
"""

pprint(home.__dict__)
# [Output] {}
"""
In above code The 'home.__dict__' instance variables is now empty.

The 'home.__dict__' stores the instance variables of the 'home' object
like the 'HtmlDocument.__dict__' stores the class variables
of the 'HtmlDocument' class.

Unlike the '__dict__' attribute of a class,
the type of the '__dict__' attribute of an instance is a dictionary.
"""

print(type(home.__dict__))
# [Ouput] <class 'dict'>
print(type(HtmlDocument.__dict__))
# [Output] <class 'mappingproxy'>

"""
Since a dictionary is mutable, you can mutate it e.g.,
adding a new element to the dictionary.

Python allows you to access the class variables
from an instance of a class.
"""
print(home.extension)
# [Output] HTML
print(home.version)
# [Output] 5

"""
In this case, Python looks up the variables 'extension' and 'version'
in 'home.__dict__' first.

If it doesn't find them there, it'll go up to the class and
look up in the 'HtmlDocument.__dict__'.

However, if Python can find the variables in the '__dict__' of the instance,
it won't look further in the '__dict__' of the class.
"""

# Defines the 'version' variable of the 'home' object
home.version = 6
HtmlDocument.version = 1
print(home.__dict__)
# [Output] {'version': 6}
print(home.version)
# [Output] 6

"""
Python adds the 'version' variable to the '__dict__' attribute
of the 'home' object.
The '__dict__' now contains one instance variable.
If you access the 'version' attribute of the 'home' object,
Python will return the value of the 'version' in the 'home.__dict__'
dictionary.
"""

HtmlDocument.media_type = "text/html"  # type: ignore
print(home.media_type)  # type: ignore
# [Output] text/html

"""
But if you change the class variables.
These changes also reflect in the instances of the class.
"""

# Initializing instance variables


# Defines the class that has two instance variables 'name' and 'contents'
class AnotherHtmlDocument:
    version = 5
    extension = "html"

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


"""
In practice, yout initialize instance variables
for all instances of a class in the '__init__' method.
When creating a new instance of the 'AnotherHtmlCodument',
you need to pass the coresponding arguments like the following.
"""

blank = AnotherHtmlDocument("Black", "")
print(blank.__dict__)
# [Output] {'name': 'Black', 'contents': ''}
print(home.__dict__)
# [Output] {'version': 6}

"""
Learn about instances variables including data variables
and function variables.

[Summary]
- Class variables are bound to a class,
  while instance variables are bound
  to a specific instance of a class.
- The instance variables are also
  called instance attributes.
- Python stores the instance variables in the '__dict__'
  attribute of the instance.
  Each instance has its own '__dict__' attribute and
  the keys in this '__dict__' may be different.
- When you access a variable via the instance, python finds
  the variable in the '__dict__' attribute of the instance.
  If it cannot find the variable, it goes up and look it up
  in the '__dict__' attribute of the class.
"""
