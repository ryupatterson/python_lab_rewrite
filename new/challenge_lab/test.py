x = "hello"
y = [byte.to_bytes(1) for byte in "hello".encode()]
print(y)