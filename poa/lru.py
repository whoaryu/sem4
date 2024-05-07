frames = []
pages = []
recent = []
hits = 0
miss = 0
index = 0


n = int(input("Enter the number of frames: "))


p = int(input("Enter the number of pages:"))
for i in range(p):
    pages.append(int(input("Enter the page number: ")))


for i in range(n):
    frames.append(-1)
    recent.append(-1)
    print(f"F{i}",end="\t")
print()


for i in range(p):
    flag = 1
    for j in range(n):
        if frames[j] == pages[i]:
            recent[j] = i
            flag = 0
            hits +=1
            break
    
    if flag:
        miss +=1
        index = recent.index(min(recent))
        frames[index]=pages[i]
        recent[index]=i
    
    for j in range(n):
        if frames[j]==-1:
            print(f"-",end="\t")
        else:
            print(f"{frames[j]}",end="\t")
    print()


print(f"Number of hits: {hits}")
print(f"Number of miss: {miss}")
