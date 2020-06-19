import zlib
a = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(a)
print(t)
print(zlib.decompress(t))