string = "😒😘😍😓😧😕😋😘😛😢😑😋😑😙😛😖😕😋😚😛😋😙😍😠😠😑😞😋😣😔😍😠😋😕😋😟😠😕😘😘😋😘😛😢😑😋😑😙😛😖😕😋🗠🗝🗣🗝🗡🗞🗝🗡🗜🗥😩"

ascii = []
for s in string:
    ascii.append(ord(s))

shifted = []
for a in ascii:
    shifted.append(a - 128428)
    
flag = []
for s in shifted:
    flag.append(chr(s))
    
for f in flag:
    print(f,end="")