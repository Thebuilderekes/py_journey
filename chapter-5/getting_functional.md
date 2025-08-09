# Functions
- Functions are as way to reuse your code so you do not have to repeat the same code blocks every time you wan to use it.
- To call a function you must have defined the function
- You can return a value from a function and store it into a variable for later use
- Variables that exist within functions are call local variables
- The default return value of a function that has no return value set is
	```````None`````````````

## Global variables

Global variables are variables that are available through out the program and can also be accessed from within functions using the `global` keyword.


## Default arguments

These are are arguments that can have a value set from the function definition so that that value is used whenever the function is called without having to set it again unless its value needs to be overridden during the function call.
`def get_address(house_no, street=lake):`

