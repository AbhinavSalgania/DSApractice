testcases = int(input())  # number of test cases

for i in range(0, testcases):
    n = int(input())  # Enter number of elements

    arr = input().split()
    for item in arr[::-1]:
        print(item, end=" ")

    print("\n")
