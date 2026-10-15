def eq_val(n):
    arr = [1] * n + [n] + [1] * n
    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])

        if left == right:
            return arr[i]
    return -1

n = int(input("Enter n:"))
print("Array:", [1] * n + [n] + [1] * n)

answer = eq_val(n)
print("Equilibrium value:", answer)