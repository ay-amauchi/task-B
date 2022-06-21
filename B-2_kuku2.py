row = int(input("行数を入力してください: "))
column = int(input("列数を入力してください: "))


for r in range(1, row + 1):
    for c in range(1, column + 1):
        answer = r * c
        print(answer, end=" ")
    print("\n", end="")
