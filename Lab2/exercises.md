# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Answer:
A well-chosen function name is a clear and concise verb that effectively communicates the action it performs. This practice enhances code readability and makes it easier for developers to understand the function's purpose and usage within the codebase.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

Answer:
Dictionary: Uses a hash table to store key-value pairs, allowing fast key-based access. Ideal for data with unique keys.

List: Utilizes dynamic arrays or linked lists to maintain ordered collections. Suitable for sequences of data where order matters.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Answer:
Yes, a list allows for random access, which means you can access any element in the list by specifying its index. Lists are ordered collections where elements are stored sequentially, and you can retrieve any element by providing its index. 

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Answer:
Pros:
Versatility
Flexibility
Interoperability
Reduced development time

Cons:
Complexity
Potential performance issues
Ambiguity
Lack of type safety
Steeper learning curve

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Answer:
  1. requests.get() - This is a well-named function. It is used for sending an HTTP GET request, and the function name clearly indicates its purpose.

  2. r.status_code - This is a appropriately named attribute for retrieving the HTTP response status code.

  3. r.headers['content-type'] - This is a sensibly named attribute for accessing the "content-type" field from the headers of an HTTP response.

  4. r.encoding - This is a well-named attribute for getting the character encoding of the HTTP response.

  5. r.text - This is a well-named attribute for retrieving the text content of an HTTP response.

  6. r.json() - This is a well-named method for parsing the JSON content of an HTTP response into a Python object.

Overall, the functions and attributes in the Requests library are named in a clear and convention-following manner, making it easy for users to understand their purpose and usage. This enhances code readability and maintainability. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Answer:
In the Requests module, some member functions have many arguments:

requests.request(method, url, **kwargs): This function is highly versatile, accepting numerous optional arguments like params, data, json, headers, cookies, files, auth, timeout, allow_redirects, proxies, verify, stream, and cert. While flexible, using many of them in one call can make the code complex.

requests.get(url, params=None, **kwargs): This function accepts params and additional optional arguments using **kwargs, potentially leading to a long argument list.

requests.post(url, data=None, json=None, **kwargs): It allows POST requests with data or JSON payloads. It includes data, json, and more optional arguments via **kwargs, offering flexibility but complexity.

These functions are powerful but require careful management of arguments for code readability and maintainability. Users should select the right arguments based on their specific requests.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

Answer:
**kwargs is a Python feature that lets a function accept any number of keyword arguments. It gathers these arguments into a dictionary.

Advantages:

Flexibility: **kwargs lets you pass multiple keyword arguments without specifying them upfront, making functions more versatile.

Forward Compatibility: You can add new keyword arguments to a function without breaking existing code.

Clarity: Using keyword arguments can make code more readable.

Disadvantages:

Lack of Explicitness: It may not be clear which arguments a function expects.

Debugging: Identifying issues with keyword arguments can be challenging.

Type Checking: Python doesn't check argument types, potentially leading to runtime errors.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Answer:
In the Requests Session class, some methods have arguments set to None by default. This is done to provide flexibility when making requests. Users can omit these arguments to use the default behavior, or they can set specific values to customize the request according to their needs. Using None as the default value allows for sensible defaults while enabling customization.