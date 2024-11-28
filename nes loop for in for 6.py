# break outer loop with inner loop value
for i in range (1,6):
    if j==3:
        break
    for j in range(1,6):
        print(i,j)
'''        
 it will give error becoz j is not defined.
'''

# break outer loop with inner loop value
for i in range (1,6):
    for j in range(1,6):
        print(i,j)
    if j==3:
        break

# loop will not break becoz from inner loop j is coming out with 5 as its value.
