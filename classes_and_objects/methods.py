#  link : https://www.pythontutorial.net/python-oop/python-methods/

# Introduction to the methods


"""
By definition, a method is a function that bound
to an instance of a class.
"""


# Defines a 'Request' class that constains a funtion 'send()'
class Request:
    def send():  # type: ignore
        print("Sent...")


# Call the 'send()' function via the 'Request' class

Request.send()
# [Output] Sent ...

Request.send
# [Output] <function Request.send at 0x000001D30F44FBA0>

id(Request.send)
# [Output] 2006005906336

hex(id(Request.send))
# [Output] '0x1d30f44fba0'

type(Request.send)
# [Output] <class 'function'>

"""
- The 'send()' is a function object.
- The 'send()' is an intance of the 'function' class.
- The type of 'send()' is function.
"""

# Create a new instance of the 'Request' class
http_request = Request()

http_request.send
# [Output] <bound method Request.send of <__main__.Request object at 0x000001D30F2D7B60>>

"""
If you display the 'http_request.send', it’ll return a bound method object.
- So the 'http_request.send()' is not a function like 'Request.send()'.
- Check if the 'Request.send' is the same object as the 'http_request.send'
  with the keyword 'is'.
- It’ll returns 'False' as expected.
"""

type(http_request.send) is (Request.send)  # type: ignore
# [Output] False

"""
The reason is that the type of the 'Request.send' is function
while the type of the 'http_request.send' is method, as shown below:
"""

type(Request.send)
# [Output] <class 'function'>
type(http_request.send)
# [Output] <class 'method'>

"""
- So when you define a function inside a class, it is purely a function.
- However, when you access that function via an object,
  the function becomes a method.
- Therefore, a method is a function that is bound to an instance of a class.

If you call the send() function via the http_request object,
you will get a TypeError as follows.
"""

http_request.send()
# [Output] TypeError: Request.send() takes 0 positional arguments but 1 was given

"""
Because the 'http_request.send' is a method that is bound to the 'http_request' object,
Python always implicitly passes the object to the method as the first argument.

The following redefines the Request class where the send function accepts a list of arguments:

class AnotherRequest:
    def send(*args):
        print('Sent', args)
"""


class AnotherRequest:
    def send(*args):
        print("Sent", args)


"""
The following calss the 'send' function from the 'AnotherRequest' class.
The 'send()' function does not receive any arguments.
However, if you call the 'send()' function from
an instance of the 'AnotherRequest' class, the 'args' is not empty.
"""

AnotherRequest.send()
# [Output] Sent ()

another_http_request = AnotherRequest()
another_http_request.send()
# [Output] Sent (<__main__.AnotherRequest object at 0x000001D30F2D4080>,)

"""
The following illustrates that the object that calls the 'send()' method
is the one that Python implicitly passes into
the method as the first argument.
"""

hex(id(another_http_request.send))
# [Output] '0x1d30f456680'
another_http_request.send
# [Output] <bound method AnotherRequest.send of <__main__.AnotherRequest object at 0x000001D30F2D4080>>

"""
The 'another_http_request' object is the same as the one
Python passes to the 'send()' method as the first argument
because they have the same memory address.

In other words, we can access the instance of the class as
the first argument inside the 'send()' method.
"""

another_http_request.send()
# [Output] Sent (<__main__.AnotherRequest object at 0x000001D30F2D4080>,)
AnotherRequest.send(another_http_request)
# [Output] Sent (<__main__.AnotherRequest object at 0x000001D30F2D4080>,)

"""
The method call 'another_http_request.send()'
is equivalent to
the function call 'AnotherRequest.send(another_http_request)'.

For this reason, a method of an object always has
the object as the first argument.
By convention, it is called 'self'.
"""


class YetAnotherRequest:
    def send(self):
        print("Sent", self)


yet_another_http_request = YetAnotherRequest()
yet_another_http_request.send()
# [Output] Sent <__main__.YetAnotherRequest object at 0x000001D30F2D69F0>
YetAnotherRequest.send(yet_another_http_request)
# [Output] Sent <__main__.YetAnotherRequest object at 0x000001D30F2D69F0>


"""
If you have worked with other programming languages
such as Java or JavaScript, the 'self' is the same as
the 'this' object.
"""

"""
Learn about Python methods and the differences between functions and methods.

[Summary]
- When you define a function inside a class,
  it is purely a function. However, when you call
  the function via an instance of a class,
  the function becomes a method.
  Therefore, a method is a function that is bound to
  an instance of a class.
- A method is an instance of the method class.
- A method has the first argument (self) as
  the object to which it is bound.
- Python automatically passes the bound object
  to the method as the first argument.
  By convention, its name is self.
"""
