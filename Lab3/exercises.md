# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is a concrete class. It is not an abstract class because it doesn't define any abstract methods and doesn't inherit from an abstract base class. In Python, concrete classes can be instantiated, while abstract classes cannot be instantiated on their own and require subclassing to provide implementations for their abstract methods.

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The commented-out __del__ method in the 'Image' class is a destructor method in Python, which is called when an object is about to be destroyed. In this case, it's empty and doesn't perform any actions during object destruction.

3. What class does Texture inherit from?
	- It's inherits from the 'Image' class.

4. What methods and attributes does the Texture class inherit from 'Image'? 
	- The constructor __init__, which initializes width, height, color channels, and pixel values.
	Also getWidth(), getHeight(), getPixelColorR(), getPixels(), and setPixelsToRandomValue().

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- The choice between 'has-a' (composition) and 'is-a' (inheritance) for the 'Texture' and 'Image' relationship depends on your application's specific requirements and how you view their connection. If 'Texture' extends 'Image,' inheritance is suitable. If 'Texture' uses 'Image' without being an 'Image,' composition is better.

6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Python does not automatically create constructors for subclasses. If a subclass doesn't declare its own constructor, it inherits the constructor of its superclass. To add specific initialization logic to a subclass, you should define your own constructor within the subclass.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

Answer:
	In Python are not inherently thread-safe by default. Because in a multi-threaded environment, if multiple threads attempt to access and potentially create the singleton instance concurrently, it can lead to race conditions and result in the creation of multiple instances, breaking the singleton pattern.