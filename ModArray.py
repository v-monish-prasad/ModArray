def modArray(A, B):
    result = 0

    for i in range(len(A)):
        result = (result * 10 + A[i]) % B

    return result


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))
    B = int(input())

    print(modArray(A, B))
