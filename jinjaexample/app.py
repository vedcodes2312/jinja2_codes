"""
jinja is a template engine for python
other template engines are django, flask etc
jinja can be used to generate html, pdf, excel, etc
jinja is used to generate dynamic content
"""

from jinja2 import Environment, FileSystemLoader

# function used directly in template
def greetfunction(name):
    return f"hello and welcome {name}"

# custom filter
def reversestring(demostr):
    return demostr[::-1]

# custom test (must return True/False)
def evenoddcheck(num):
    return (num % 2) == 0

# functions used inside loop
def printsquare(num):
    return num ** 2

# global function
def shout(demostring):
    return demostring.upper() + "!!!!"

env = Environment(loader=FileSystemLoader("templates"))

env.filters["reverse"] = reversestring
# filters - custom functions used in template 
# tests - custom functions used in template
# globals - custom functions used in template
"""
Here is the naming with operator style:

Filters → `|` (pipe operator): modifies values → `{{ name | upper }}`
Tests → `is` (identity test operator): checks conditions → `{{ num is odd }}`
Globals → `()` (function call operator): calls global Python functions → `{{ greet("Ved") }}`

"""
env.tests["evenodd"] = evenoddcheck
env.globals["shout"] = shout

template = env.get_template("demo.html")

output = template.render(
    name="xyzpqrs",
    text="JINJA2",
    num=20,
    nums=[2,3,4,5,6],
    greet=greetfunction,
    square=printsquare
)

print(output)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(output)
