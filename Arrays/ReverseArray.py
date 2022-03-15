testcases = int(input())  # number of test cases
print("Enter numbers with space in them")
if testcases <= 100:
    for i in range(0, testcases):

        arr = input().split()
        for item in arr[::-1]:
            print(item, end=" ")

        print("\n")
else:
    print("Error: Enter a number less than or equal to 100")
