height = float(input(f"身長を入力してください(cm):"))
weight = float(input(f"体重を入力してください(kg):"))

height_m = height / 100

bmi = weight / (height_m * height_m)

bmi = round (bmi,1)

print(f"BMI:",bmi)

if bmi < 18.5:
    print ("判定: 低体重")
elif bmi < 25:
    print ("判定: 普通体重")
elif bmi < 30:
    print ("判定: 肥満(1度)")
else:
    print ("判定: 肥満(2度以上)")