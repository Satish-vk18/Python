# patterns printing to get strong in loops
# -------------------------------------------
# points:
# 1.outer loop will focus on the no.of rows
# 2.inner loop will focus on the columns and make the connection with rows
# 3.print statements will be in inner loop
# 5.observe symmetry(optional)
# ---------------------------------------------

# * * * *
# * * * *
# * * * *
# * * * *

for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# * * * * * 
# * * * *
# * * *
# * *
# *

for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j,end=" ")
    print()

#        *
#      * * *
#    * * * * * 
#  * * * * * * *

for i in range(5):
    # spaces
    for j in range(5-i-1):
        print(" ",end = " ")
    # stars
    for j in range(i*2+1):
        print("*",end=" ")
    # spaces
    for j in range(5-i-1):
        print(" ",end = " ")
    print()

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range(5):
    # spaces
    for j in range(i):
        print(" ",end = " ")
    # stars
    for j in range((5*2)-(i*2)-1):
        print("*",end=" ")
    # spaces
    for j in range(i):
        print(" ",end = " ")
    print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range(5):
    # up traingle
    # spaces
    for j in range(5-i-1):
        print(" ",end = " ")
    # stars
    for j in range(i*2+1):
        print("*",end=" ")
    # spaces
    for j in range(5-i-1):
        print(" ",end = " ")
    print()
for i in range(5):
    # down traingle
    # spaces
    for j in range(i):
        print(" ",end = " ")
    # stars
    for j in range(5*2-i*2-1):
        print("*",end=" ")
    # spaces
    for j in range(i):
        print(" ",end = " ")
    print()


# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(3):
#     for j in range(3-i):
#         print("*",end=" ")
#     print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n = 5
for i in range(1,2*n):
    if i > n: i = 2*n-i
    for j in range(i):
        print("*",end=" ")
    print()

# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 

for i in range(1,6):
    s = 1
    if i%2==0:s=0
    for j in range(i):
        print(s, end = " ")
        s=1-s
    print()

# 1             1 
# 1 2         2 1 
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1 

space = 2*(5-1)
for i in range(1,5):
    # numbers
    for j in range(1,i+1):
        print(j,end=" ")
    # spaces
    for j in range(1,space-1):
        print(" ",end=" ")
    # numbers
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    space = space - 2
    
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
n = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n = n + 1
    print()

# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

for i in range(1,6):
    for j in range(6-i):
        print(chr(65+j),end=" ")
    print()

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

for i in range(5):
    for j in range(i+1):
        print(chr(65 + i),end="")
    print()

#       A       
#     A B A     
#   A B C B A   
# A B C D C B A 

for i in range(4):
    # spaces
    for j in range(4-i-1):
        print(" ",end=" ")
    # characters
    char = ord('A')
    for j in range(i*2+1):
        print(chr(char),end=" ")
        if j < i: char += 1 
        else: char -= 1
    # spaces
    for j in range(4-i-1):
        print(" ", end=" ")
    print()

# E 
# D E 
# C D E 
# B C D E 
# A B C D E 

for i in range(5):
    start = 65 + 5 - 1 - i
    for j in range(i+1):
        print(chr(start+j),end=" ")
    print()

# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 

start = 0
for i in range(5):
    # stars
    for j in range(5-i):
        print("*",end=" ")
    # spaces
    for j in range(start):
        print(" ",end=" ")
    # stars
    for j in range(5-i):
        print("*",end=" ")
    start +=2
    print()
start = 2*5-2
for i in range(5):
    # stars
    for j in range(i+1):
        print("*",end=" ")
    # spaces
    for j in range(start):
        print(" ",end=" ")
    # stars
    for j in range(i+1):
        print("*",end=" ")
    start -=2
    print()

# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

spaces = 2*5
for i in range(2*5-1):
    # stars
    if i<5 :
        stars = i+1
        spaces -=2
    else:
        stars = 2*5-i-1
        spaces +=2
    for j in range(stars):
        print("*",end=" ")
    # spaces
    for j in range(spaces):
        print(" ",end=" ")
    # stars
    for j in range(stars):
        print("*",end=" ")
    print()

# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or j == 0 or j == 5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#               1               
#             2 3 2             
#           3 4 5 4 3           
#         4 5 6 7 6 5 4         
#       5 6 7 8 9 8 7 6 5       
#     6 7 8 9 10 11 10 9 8 7 6     
#   7 8 9 10 11 12 13 12 11 10 9 8 7   
# 8 9 10 11 12 13 14 15 14 13 12 11 10 9 8 

start = 1
for i in range(8):
    # spaces
    for j in range(8-1-i):
        print(" ",end=" ")
    # numbers
    point = start
    for j in range(i*2+1):
        print(point,end=" ")
        if j >= i : point-=1
        else:point+=1
    # spaces
    for j in range(8-1-i):
        print(" ",end=" ")
    start+=1
    print()