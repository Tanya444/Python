"""
 def function_name(parameter: data_type) -> return_type:
    # body of the function
    return expression or if simply return means None object
"""
def add(num1: int, num2: int) ->int:
    """function to add 2 numbers"""
    result=num1+num2
    return result
a,b=4.3,3
ans=add(a,b)         #python automaticaly do typeconversion here as it is dynamically typed and not enforce strict
#type checks at runtime
print(ans)
print(add.__doc__)
#lambda keyword-anonymous functions
cube=lambda x: x*x*x
print(cube)
print(cube(3))
"""modules(definiions,statements) are used using import keyword, pip install library_name"""
#Pass by Object reference in functions but we can modify only if it is mutable
#list,dict,set are mutable but int,float,string,tuple is immutable(link gets broken if we try to modify)