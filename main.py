def update_bit(A, B):

    Lo = 1 << B
    if A & Lo:
        A = A ^ Lo
    return A
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
result = update_bit(A, B)
print("Output:", result)
