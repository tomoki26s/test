number = int(input("数値を入力してください:"))
if number < 0 or number > 100:
    print("無効な点数です")
elif number >= 90:
    print("評価: S")
elif number >= 70:
    print("評価: A")
elif number >= 50:
    print("評価: B")
else:
    print("評価: C")