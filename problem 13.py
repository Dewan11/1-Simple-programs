bytes = float(input("Enter bytes: "))

kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024

print(bytes, "bytes is equal to", kb, "KB")
print(bytes, "bytes is equal to", mb, "MB")
print(bytes, "bytes is equal to", gb, "GB")