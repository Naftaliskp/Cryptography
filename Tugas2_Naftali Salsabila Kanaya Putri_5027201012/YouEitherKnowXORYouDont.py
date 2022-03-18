from pwn import xor

secret = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
format = "crypto{"
find = format.encode('utf-8')

print(xor(find, secret))

coba = "myXORkey"
finding = coba.encode('utf-8')

print(xor(finding, secret))

