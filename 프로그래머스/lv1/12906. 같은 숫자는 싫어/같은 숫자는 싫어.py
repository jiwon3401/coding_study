def solution(arr):
    stack = []
    stack.append(arr[0])
    for i in range(1,len(arr)):
        stack.append(arr[i])
        if arr[i] == arr[i-1]:
            stack.pop()
        else:
            continue

    return stack