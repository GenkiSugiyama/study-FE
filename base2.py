# 変数の応用
animal = "dog"
print(animal)

# 定数 pythonでは全部大文字がルール
LEGAL_AGE = 20
age = 18

if age < LEGAL_AGE:
  print('未成年')
else:
  print('成人')

# format関数の特殊な書き方
print(f'age = {age}') #python3.6以上
print(f'{age=}') #python3.8以上　『変数名＝』で『変数名＝中身』と表示される