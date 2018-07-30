# Kickstart Round D 2018
_Problem discription:_  *https://code.google.com/codejam/contest/6364486/dashboard*

## Problem A
_for small case_
--
- Because of no negative value, iterate left position
- For each left position, binary search right position
- **O(NlogN)**

_for large case_ (not implement)
--
- Given two pointer, left and right and make the odd number large enough
- move the right and change left, use balanced binary tree to support 
- **O(NlogN)**

## Problem B
_for small case_
--
- Iterate each tower and each balloon, calculate cover or not

- **O(NK)**

_for large case_
--

- First, sort towers by x-axis.
- Then add and remove towers that not useful (not useful means one tower can cover another). 
- Last, for each balloon, use binary search to find the closest left and right tower then calculate cover or not

- **O((N+K)logN)**