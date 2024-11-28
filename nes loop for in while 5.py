# break outer loop with inner loop value.
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if j==5:
            break
    i+=1

'''
# process
1.intialize i=1.
2.By using while loop i<6.
3.inner loop By using for loop (j) fetching each element in range (1,6).
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the fetching, printing is done first then checking.
            if j==5     true
            break

3.the output is 11 12 13 14 15.
'''
