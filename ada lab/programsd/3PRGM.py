#3PRGM 
def toh(n,source,temp,dest):
    global count
    if n>0:
        toh(n-1,source,dest,temp)
        print(f"Move disk {n} {source}->{dest}")
        count+=1
        toh(n-1,temp,source,dest)
source="s"
temp="t"
dest="d"
count=0
n=int(input("Enter the number of disks:"))
print("Sequence is:")
toh(n,source,temp,dest)
print("The Number of Moves:",count)