# 8. Given two integers A and B (A ≤ B).
# Print all numbers from A to B inclusively.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
for a in range(a, b+1):
    print(a)
