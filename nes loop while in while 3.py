# break inner loop with outer loop value.
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1
    i+=1

'''
# process
1.initialiging i=1.
2.By using while loop i<6.
3.initialiging j=1.
4.inner loop By using while loop i<6.
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the fetching, printing is done first then checking.
            if i==3     false
            
Iteration 2:print(i,j) here outer loop i=2 and j inner loop j gets iterated 21 22 23 24 25.
            here the fetching, printing is done first then checking.
            if i==3      false
         
Iteration 3:print(i,j) here outer loop i=3 and j inner loop j gets iterated 31.s
            here the fetching, printing is done first then checking.
            if i==3      true
            break
Iteration 4:print(i,j) here outer loop 1=4 and j inner loop j gets iterated 41 42 43.
            here the fetching, printing is done first then checking.
            if i==3      false
            
Iteration 5:print(i,j) here outer loop 1=5 and j inner loop j gets iterated 51 52 53.
            here the fetching, printing is done first then checking.
            if i==3      false
           
3.the output is 11 12 13 14 15 21 22 23 24 25 31 41 42 43 44 45 51 52 53 54 55.
'''

