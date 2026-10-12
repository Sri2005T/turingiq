def boundry(mat,n,m):
    arr = []
    for i in range(m):
        arr.append(mat[0][i])
    
    for i in range(1,n):
        arr.append(mat[i][m-1])

    for i in range(m-2,-1,-1):
        arr.append(mat[n-1][i])  

    for i in range(n-2,0,-1):
        arr.append(mat[i][0])  
         
    return arr
mat = [
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],   
[16,17,18,19,20]
]


print(boundry(mat,4,5))