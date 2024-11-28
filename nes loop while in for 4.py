# break outer loop with outer loop value.
for i in range(1,6):
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        j+=1
'''
# process
1.By using for loop (j) fetching each element in range (1,6).
2.initialiging j=1.
3.inner loop By using while loop i<6.
Iteration 1:print(i,j) here outer loop i=1.
            here the fetching,checking is done first then printing.
            if i==3     false
            j inner loop j gets iterated 11 12 13 14 15
Iteration 2:print(i,j) here outer loop i=2.
            here the fetching,checking is done first then printing.
            if i==3      false
            j inner loop j gets iterated 21 22 23 24 25.
Iteration 3:print(i,j) here outer loop i=3.
            here the fetching,checking is done first then printing.
            if i==3      true.
            break           
3.the output is 11 12 13 14 15 21 22 23 24 25.
'''
