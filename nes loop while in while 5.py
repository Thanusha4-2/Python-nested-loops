# break outer loop with inner loop value.
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break    
    i+=1

'''
# process
1.initialiging i=1.
2.By using while loop i<6.
3.initialiging j=1.
4.inner loop By using while loop i<6.
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the fetching, printing is done first then checking.
            if j==6     true
            break

3.the output is 11 12 13 14 15.
'''
