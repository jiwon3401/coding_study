def solution(arr1, arr2):
    #행렬 크기: len(arr1) * len(arr2[0])
    answer = [len(arr2[0])*[0] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])): #(i*k)*(k*j)
                answer[i][j]+= arr1[i][k]*arr2[k][j]
        
    return answer