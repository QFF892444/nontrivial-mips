
print("$3=0x00000400")
print("skip")
print("skip")
print("$29=0xbfc00000")
print("skip")
z = 0
for i in range(0, 0x400 + 1):
    z += i
    print("skip\n$1=0x%08x\n$2=0x%08x" % (z, i + 1))
print("skip")
