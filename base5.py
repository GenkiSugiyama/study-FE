# 2進数、8進数、16進数について

# ●進数を10進数に
a = 0b100 # 「0b + 2進数の値」と入力すると「0b」以下の数値が2進数と見なされる
print(a)

b = 0o11 # 0o」で8進数
print(b) # 9
c = 0x10 # 「0x」で16進数
print(c) # 16

# 10進数を●進数（文字列）に
print(bin(4)) #0b100 bin()で2進数
print(type(bin(4)))

print(oct(9)) # 0o11 oct()で8進数
print(hex(9)) # 0x9 hex()で16進数