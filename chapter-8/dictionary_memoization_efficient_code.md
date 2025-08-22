## Recursion vs Iteration in Python

- **Recursion** is a technique where a function calls itself to solve smaller instances of the same problem. It’s elegant and often easier to write for problems naturally defined in terms of smaller subproblems (like tree traversals, divide-and-conquer algorithms).

- **Iteration** uses loops to repeat a block of code until a condition is met. It’s typically more straightforward and uses less memory.

**Efficiency considerations:**

- **Memory:** Recursion uses the call stack to keep track of function calls, which can lead to higher memory use and risk of hitting Python’s recursion depth limit for large inputs. Iteration usually uses a fixed amount of memory.

- **Speed:** Iterative solutions tend to be faster because function calls add overhead. Python doesn’t optimize tail-recursion, so recursive calls can be slower.

**When to use which?**

- Use **recursion** when the problem is naturally recursive, the input size is small or medium, and clarity/readability is more important.

- Use **iteration** when performance and memory efficiency are critical, especially for large datasets or performance-sensitive code.

## Dictionaries

##Memoization

Memoization is the process of caching the results of memory heavy functions for later use to in order to provide efficiency in your code.

Expensive functions, that is functions that use up a lot of memory and take time to execute need not be executed all the time, instead, their return value can be cached so they can be reused as needed.
