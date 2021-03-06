# algorithms
[![Build Status](https://travis-ci.org/AndreiRegiani/algorithms.svg?branch=master)](https://travis-ci.org/AndreiRegiani/algorithms)

### Problem 1
```
Write a program that takes a list of strings containing integers and
words and returns a sorted version of the list. The output should maintain the
positions of strings and numbers as they appeared in the original string.

Input : car truck 8 4 bus 6 1
Output: bus car 1 4 truck 6 8

(...) full description on /problem-1/description.txt
```

### Problem 2
```
You are given an array which will have a length of at least 3,
but could be very large. The array is either entirely comprised of odd integers
or entirely comprised of even integers except for a single integer N.
Write a function that takes the array as an argument and returns N.

Input  : [2, 4, 0, 100, 4, 11, 2602, 36]
Output : 11

(...) full description on /problem-2/description.txt
```
Benchmarks comparing performance of different implementations: [See Benchmarks 1](https://github.com/Hackermen/python-experiments)

### Problem 3
```
Write a function that takes a message and reverses the order
of the words *in-place*.

Input : others on depend not do salvation own your out work
Output: work out your own salvation do not depend on others
```

### Problem 4
```
Write three functions that compute the sum of the numbers in a
given list using a for-loop, a while-loop, and recursion.

Input : [2, 3, 5, 10, 80]
Output: 100
```

### Problem 5
```
Write a function that combines two lists by alternatingly taking elements.

Input : ['a', 'b', 'c'], ['1', '2', '3']
Output: ['a', '1', 'b', '2', 'c', '3']
```

### Problem 6
```
Write a function that given a list of non-negative integers,
arranges them such that they form the largest possible number.

Input  : [50, 2, 1, 9]
Output : 95021
```

### Problem 7
```
Find out which one of the given numbers differs from the others.

Input  : "2 4 7 8 10"
Output : 3

Input  : "1 2 1 1"
Output : 2
```

### Problem 8
```
Given an array containing hashes of names
Return a string formatted as a list of names separated by commas except for
the last two names, which should be separated by an ampersand.

Input : [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
Output: 'Bart, Lisa & Maggie'

Input : [{'name': 'Bart'}, {'name': 'Lisa'}]
Output: 'Bart & Lisa'

Input : [{'name': 'Bart'}]
Output: 'Bart'
```

### Problem 9
```
Complete the method/function so that it converts dash/underscore delimited
words into camel casing. The first word within the output should be capitalized
only if the original word was capitalized.

Input : "the_stealth_warrior"
Output: "theStealthWarrior"

Input : "The-Stealth-Warrior"
Output: "TheStealthWarrior"
```

### Problem 10
```
Write a function cakes(), which takes the recipe (dict) and the available
ingredients (dict) and returns the maximum number of cakes Pete can
bake (integer).

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
Input : cakes(recipe, available)
Output: 2
```
