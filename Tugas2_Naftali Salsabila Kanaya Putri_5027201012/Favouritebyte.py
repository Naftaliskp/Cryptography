from pwn import xor

secret = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(256):
    flag = xor(i, secret)
    find = "crypto"
    find = find.encode('utf-8')
    if find in flag:
        print(flag)
        break;