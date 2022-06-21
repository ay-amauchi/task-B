"""
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること

"""
import random

N_men = int(input("サイコロの面の数は?:"))
M_times = int(input("何回振りますか?: "))

numbers_list = list()

for r in range(0, M_times):

    dice = random.randint(1, N_men)
    numbers_list.append(dice)

print(numbers_list)
