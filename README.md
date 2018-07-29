# Kickstart Round D 2018
_Problem discription:_  *https://code.google.com/codejam/contest/6364486/dashboard*

## Problem B
_for small case_
--
_methods_ 
> Iterate each tower and each balloon, calculate cover or not

_time cost_
**O(NK)**

_for large case_
--
_methods_
> First, sort towers by x-axis.
> Then add and remove towers that not useful (not useful means one tower can cover another). 
> Last, for each balloon, use binary search to find the closest left and right tower then calculate cover or not

_time cost_
**O((N+K)logN)**