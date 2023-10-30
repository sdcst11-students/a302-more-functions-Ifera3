#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math

def triangle(A,B,C):
    c = max(A,B,C)
    a = min(A,B,C)
    b = (A+B+C) - a - c
    if a + b < c:
        return 0
    elif (a**2) + (b**2) > (c**2):
        return 1
    elif (a**2) + (b**2) == (c**2):
        return 2
    elif (a**2) + (b**2) < (c**2):
        return 3

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
