from string import ascii_lowercase as lowercase
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = "map"
print(list(s))
print(lowercase)
s = list(s)
for i in range(len(s)):
    if s[i] not in lowercase:
        continue
       
    s[i] = chr(ord(s[i]) + 2)
    # print(chr(ord(c)))
    # prinord(c)+4)
print(s)
print(''.join(s))
print(ord(" "))


