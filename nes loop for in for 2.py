# break inner loop with inner loop value
for i in range (1,6):
     for j in range(1,6):
            print(i,j)
            if j==3:
                 break

'''
# process
1.By using for loop (i) fetching each element in range (1,6).
2.inside for By using for loop (j) fetching each element in range (1,6).
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13.
            here the fetching, printing is done first then checking.
            if j==3      true
            break
Iteration 2:print(i,j) here outer loop i=2 and j inner loop j gets iterated 21 22 23.
            here the fetching, printing is done first then checking.
            if j==3      true
            break
Iteration 3:print(i,j) here outer loop i=3 and j inner loop j gets iterated 31 32 33.
            here the fetching, printing is done first then checking.
            if j==3      true
            break
Iteration 4:print(i,j) here outer loop 1=4 and j inner loop j gets iterated 41 42 43.
            here the fetching, printing is done first then checking.
            if j==3      true
            break
Iteration 5:print(i,j) here outer loop 1=5 and j inner loop j gets iterated 51 52 53.
            here the fetching, printing is done first then checking.
            if j==3      true
            break
3.the output is 11 12 13 21 22 23 31 32 33 41 42 43 51 52 53.
'''
