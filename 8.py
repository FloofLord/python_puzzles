import zipfile
# ANnswer is hockey
# real answer O X Y G E N
data = {}
# archive.getinfo("firstobj.1").comment
with zipfile.ZipFile('channel.zip') as myzip:
    # print(myzip.filelist)
    for file in myzip.filelist:
       
        with myzip.open(file) as myfile:
            #print(myzip.getinfo(myfile.name).comment)
            data[myfile.name.replace(".txt","")] = (myfile.read().decode().split(" ")[-1], myzip.getinfo(myfile.name).comment)
            


print(data)
comments = []
next = "90052"
while True:
    print(next)
    try:
        next = data[next]
    except:
        break
    comments.append(next[1].decode())
    next = next[0]
    #print(f"new next is {next}")
    
print("".join(comments))   
    
    
    
# d = []
# for n in data:
#     n = n.split(" ")[-1]
#     try:
#         d.append(int(n))
#     except:
#         pass
# #90052
# d = sorted(d)

# for i in d:
#     print(i)
# for i in range(len(d)):
#     print(d[i])
#     if d[i] == 90052:
#         print(i, d[i])
    
    


