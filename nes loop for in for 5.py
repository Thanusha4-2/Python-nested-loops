# break outer loop with outer loop value
for i in range (1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
        


'''
# process 
1.By using for loop (i) fetching each element in range (1,6).
2.inside for By using for loop (j) fetching each element in range (1,6).
Iteration 1:print(i,j) here outer loop i=1 and j inner loop j gets iterated 11 12 13 14 15.
            here the checking is done first,then printing.
            if i==3     false
            
Iteration 2:print(i,j) here outer loop i=2 and j inner loop j gets iterated 21 22 23 24 25.
            here the checking is done first,then printing.
            if i==3      false
           
Iteration 3:print(i,j) here outer loop i=3 and j inner loop j gets iterated 31 32 33 34 35.
            here the checking is done first,then printing.
            if i==3      true
            break
3.the output is 11 12 13 14 15 21 22 23 24 25.
'''

