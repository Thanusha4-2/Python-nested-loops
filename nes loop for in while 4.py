# break outer loop with outer loop value
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if i==3:
            break
    i+=1

'''
i=1
while i<6:
    if i==3:
        break
    for j in range (1,6):
        print(i,j)   
    i+=1
ouput : 11 12 13 14 15 21 22 23 24 25. // here the fetching and checking done first and then printing.
# process
1.intialize i=1.
2.By using while loop i<6.
3.inner loop By using for loop (j) fetching each element in range (1,6).
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the fetching, printing is done first then checking.
            if i==3     false
            
Iteration 2:print(i,j) here outer loop i=2 and j inner loop j gets iterated 21 22 23 24 25.
            here the fetching, printing is done first then checking.
            if i==3      false
            
Iteration 3:print(i,j) here outer loop i=3 and j inner loop j gets iterated 31 32 33 34 35.
            here the fetching, printing is done first then checking.
            if i==3      true
            break
3.the output is 11 12 13 14 15 21 22 23 24 25 31 32 33 34 35.
'''
