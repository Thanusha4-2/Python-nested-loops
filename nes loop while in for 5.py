# break outer loop with inner loop value.
for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
    if j==3:
        break
        j+=1
'''
# process
1.By using for loop (j) fetching each element in range (1,6).
2.initialiging j=1.
3.inner loop By using while loop i<6.
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the fetching, printing is done first then checking.
            if j==6     true
            break
3.the output is 11 12 13 14 15.
'''
