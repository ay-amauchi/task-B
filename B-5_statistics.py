# リスト
numbers = input(("データを入力してください(スペース区切り) > ")).split()

# 合計値
sum_number = 0
for r in range(0, len(numbers)):
    number = int(numbers[r])
    sum_number += number

print(f"合計値: {sum_number}")

# 最大値
max_number = 0
for r in range(0, len(numbers)):
    num = int(numbers[r])
    if num > max_number:
        max_number = num

print(f"最大値: {max_number}")

# 最小値
min = 0
for r in range(0, len(numbers)):
    if numbers[min] > numbers[r]:
        min = r

print(f"最小値: {numbers[min]}")

# 平均値
average = sum_number / len(numbers)
print(f"平均値: {average}")
