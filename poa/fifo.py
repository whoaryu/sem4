frames = []
pages = []
hits = 0
miss = 0
index = 0


n = int(input("Enter the number of frames: "))


p = int(input("Enter the number of pages:"))
for i in range(p):
    pages.append(int(input("Enter the page number: ")))


for i in range(n):
    frames.append(-1)
    print(f"F{i}",end="\t")
print()


for i in range(p):
    flag = 1
    for j in range(n):
        if frames[j] == pages[i]:
            flag = 0
            hits +=1
            break
    
    if flag:
        miss +=1
        frames[index] = pages[i]
        index = (index+1)%n


    
    for j in range(n):
        if frames[j]==-1:
            print(f"-",end="\t")
        else:
            print(f"{frames[j]}",end="\t")
    print()


print(f"Number of hits: {hits}")
print(f"Number of miss: {miss}")
