numbers = input(("データを入力してください(スペース区切り) > ")).split()

sum_number = 0
for r in range(0, len(numbers)):
    number = int(numbers[r])
    sum_number += number

print(f"合計値: {sum_number}")

for r in range(0, len(numbers)):
    max_number = int(numbers[r])
    if max_number 
    

print(f"最大値: {max(numbers)}")
print(f"最小値: {min(numbers)}")

average = sum_number / len(numbers)
print(f"平均値: {average}")
