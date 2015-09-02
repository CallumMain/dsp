# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

The main difference between lists and tuples in python is that tuples are immutable and lists are mutable.  This means that items cannot be added or removed from a tuple.  However you can use the 'in' operator and find items in a tuple just like in lists.  Some tuples can be used as keyes in dictionaries if they contain immutable values, lists can never be used as keys in dictionaries because they are not immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

The main difference between lists and sets is that lists can have duplicates and sets cannot.  Sets also require items to be hashable and does not preserve order like lists do.

> l = [1,2,3,4]
> l.append(5)
[1,2,3,4,5]

>s = set("Metis")
>'t' in s
True

Sets are faster for determining whether or not they contain an element but slower for iterating over, this is because they are implemented hash tables which have constant time for look up in the average case.  Lists are slightly faster for iterating.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambdas are anonymous fuctions that are used to define a function in line that might be difficult to define the normal way.  For instance rather than normally defining like:
> def add(a,b):
>> return a + b

We can instead write:
> lambda a, b: a+b

We can also use it as an argument in fuctions that expect a function such as sorted()'s key argument:
> sorted([[3, 4], [3, 5], [1, 2], [7, 3]], key=lambda x: x[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is a very concise way of creating new lists.  It is commonly used to make new lists where each element is the result of some operation applied to a sequence or iterable.  For example if we wanted to create a list of all of the squares for integers less than 10:
> squares = [x**2 for x in range(10)]

This is equivalent to:
> squares = map(lambda x: x**2, range(10))

List comprehension is the 'pythonic' way to create lists as its more concise and easier to read.  One thing to note is that because map requires a function/lambda as and argument, it introduces a new scope and doesn't overwrite x like list comprehension does.

Comprehension can also be done for other data structures such as sets and dictionaries.  For example:
>{x for x in 'abracadabra' if x not in 'abc'}
set(['r','d'])

>{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





