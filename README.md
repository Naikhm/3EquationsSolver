# 3EquationsSolver

My first mathy project,it solves 3 linear equations with 3 variables using gussian elimination (matrices) and the code is unfortunately brute forcing it because im still not used to coding (only 1 month in it) but i see this as a big jump,hope you like it and leave some advices if you can besically what it does is puting the coeffecient of the 3 variables of the 3 equations in a matrix called (the gussian matrix i think) and it look like this:
```python
[x11 y12 z13 | d1]
[x21 y22 z23 | d2]
[x31 x32 z33 | d3]
where x,y,z are the coeffecint of each equation and the d1,d2,d3 are the answers of each equation.
in the code because it was brute force i did the maath the way i did in school when we learnt it,
and its by multipling rows by a certian number and adding the whole row to another row,
this operatios has to be done untill the matrix is like:
[x11 y12 z13 | d1]
[ 0  y22 z23 | d2]
[ 0   0  z33 | d3]
so in the end of the code z33 = d3 is the value of z and x,y are found easily after that
example:
[1 1  1 |-1]
[1 1 -1 | 1]
[2 3  4 | 6]
(row 1 * -2) + row 3
[1 1  1 |-1]
[1 1 -1 | 1]
[0 1  2 | 8]
(row 1 * -1) + row 2
[1 1  1 |-1]
[0 0 -2 | 2]
[0 1  2 | 8]
in here the code will swap row 2 and row 3 
[1 1  1 |-1]
[0 1  2 | 8]
[0 0 -2 | 2]
and wee are done
-2z = 2 ----> z = -1
y + 2z = 8 ----> y + 2(-1) = 8 ----> y = 10
x + 10 + -1 = -1 ----> x = -10
tbh am proud this code lmao,so any advice you could give me,i would appretiate it :)
```

