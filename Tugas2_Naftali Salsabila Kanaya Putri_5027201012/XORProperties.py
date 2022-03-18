from pwn import xor
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" 
KEY21 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FKEY123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

byte1 = bytes.fromhex(KEY1)
byte21 = bytes.fromhex(KEY21)
byte23 = bytes.fromhex(KEY23)
byteF123 = bytes.fromhex(FKEY123)

KEY123 = xor(byte1, byte23)
FLAG = xor(byteF123, KEY123)

print(FLAG)
