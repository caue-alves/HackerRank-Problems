# Introduction to Sets
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Example
```
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Basically, sets are used for membership testing and eliminating duplicate entries.
```
# Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used:

Average = sum of Distinct Heights / Total Number of Distinct Heights

# Input Format

The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.

# Constraints
0 < N < 100

# Output Format

Output the average height value on a single line.

# Sample Input
```
10
161 182 161 154 176 170 167 171 170 174
```
# Sample Output
```
169.375
```
# Explanation

Here, set `([154, 161, 167, 170, 171, 174, 176, 182])` is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

Average = 1355/8 = 169.375