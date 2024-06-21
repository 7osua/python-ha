# link: https://www.pythontutorial.net/python-oop/python-class-variables/

from pprint import pprint


# Introduction to the Class Variables
class HtmlDocuments:
    extension = "html"
    version = "5"

    def render():  # type: ignore
        print("Rendering the HTML doc ...")


"""
Everything in python is an object including a class.
When we define a class using the 'class' keyword,
Python creates an object with the name the same
as the classes name.

In this example
- We defines the 'HtmlDocuments' class and the 'HtmlDocuments' object.
- The 'HtmlDocuments' object has the '__name__' property.
- The 'HtmlDocuments' object has the type of 'type'.
- The 'HtmlDocuments' is an instance of the 'type' class.
"""

print(HtmlDocuments.__name__)
print(type(HtmlDocuments))
print(isinstance(HtmlDocuments, type))
"""
- Class variables are bound to the class.
- They are shared by all instances of that class.
- Both the 'extension' and 'version' are the class variables
  of the 'HtmlDocuments' class.
  In other words, both of the class variables are bound to
  the 'HtmlDocuments' class.
"""


# Get the values of class variables
print(HtmlDocuments.extension)
print(HtmlDocuments.version)

extension = getattr(HtmlDocuments, "extension")
version = getattr(HtmlDocuments, "version")
"""
- To get the values of class variables, we can use the '.' dot notation.
- Another way to get the value of a class variable is use
  the 'getattr()' function.
- The 'getattr()' function accepts an object an a variable name.
  It returns the value of class variable.
"""

print(HtmlDocuments.media_type)  # AttributeError # type: ignore
"""
- If we access a class variable that does not exist,
  the 'AttribureError' exception will raise.
"""

media_type = getattr(HtmlDocuments, "media_type", "text/html")
print(f"extension = {extension}\nversion = {version}\nmedia_type = {media_type}")

"""
- To avoid exception, we can specify a default value if the class variable
  does not exist.
"""


# Set values for class variables
HtmlDocuments.version = "4.0"
setattr(HtmlDocuments, "version", "5.0")
"""
- To set a value for class variable, we can use the dot notation.
- Or we can use the 'setattr()' built-in function.
"""

HtmlDocuments.media_type = "text/json"  # add a new class variable. # type: ignore
setattr(HtmlDocuments, "media_type", "text/html")  # set a value to the class variable.
"""
Since python is a dynamic language, we can add a class variable
to a class at runtime after we created it.

In the example above, we add the 'media_type' class variable
to the 'HtmlDocuments' class, After we define it.
"""


# Delete class variables
delattr(HtmlDocuments, "media_type")
del HtmlDocuments.version

"""
- To delete a class variable at runtime, we use the 'delattr()' function.
- Or we can use the 'del' keyword.
"""

# Class variable storage

pprint(HtmlDocuments.__dict__)
"""
- Python stores class variables in the '__dict__' attribute.
- The '__dict__' attribute is mapping proxy, which is a dictionary.
- As clearly shown in the output, the '__dict__' has three class variables:
  'extension', 'media_type', 'version', and 'render()' besides other predefined class variables.
  Python does not allow us to change the '__dict__' directly, and will result an 'TypeError' error.
"""
HtmlDocuments.__dict__["realesed"] = "2008"  # TypeError
setattr(HtmlDocuments.__dict__, "realesed", "2008")  # TypeError
pprint(HtmlDocuments.__dict__)
"""
However, you can use the 'setattr()' function or '.' dot notation to
indirectly change the '__dict__' attribute.

Also, the key of the '__dict__' are strings that will help Python
speeds up the variable lookup.

[Note] :
Although Python allows you to access class variables through the '__dict__' dictionary,
it is not a good practice. Also, it will not work in some situations!
"""


# Callable class attribute
"""
- Class attributes can be any object such as a function.
- When you add a function to a class,
  the function become class attribute.
  Since a function is callable, the class attribute is called
  a callable class attribute.
"""

pprint(HtmlDocuments.__dict__)
HtmlDocuments.render()

"""
In this example, the 'render()' is a class attribute of the 'HtmlDocuments' class.
Its value is a function.
"""

"""
Learn how the class variables (or attributes) work.
- A class is an object which is an instance of the 'type' class.
- Class variables are attributes of the 'class' object.
- Use the '.' dot notation or 'getattr()' function
  to get the value of a class attribute.
- Use the '.' dot notation or 'setattr()' function
  to set the value of a class attribute.
- Python is a dynamic language. Therefore, you can assign a class variable
  to a class at runtime.
- Python strore class varables in the '__dict__' attribute.
  The '__dict__' attribute is a dictionary.
"""
