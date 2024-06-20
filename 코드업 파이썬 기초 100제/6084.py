h, b, c, s = map(float, input().split())
Byte = 8
MB = 2**10 * 2**10  * Byte
needByte = (h*b*c*s)/MB
print("{:.1f} MB".format(needByte), end=' ')
