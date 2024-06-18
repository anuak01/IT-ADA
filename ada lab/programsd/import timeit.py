import timeit
import matplotlib.pyplot as plt

def Input (array,n):
    for i in range(0,n):
        ele=int(input("ARR:"))
        array.append(ele)
def binary_search(array,key):
    while len(array)>0:
        mid=(len(array))//2
        if array[mid]==key:
            return True
        elif array[mid]<key:
            array=array[:mid]
        else:
            array=array[mid+1:]
        return False
N=[]
CPU=[]
trail=int(input("Enter no of trails:"))
for t in range(0,trail):
    array=[]
    print("-------> TRAIL NO",t+1)
    n=int(input("Enter number of elements:"))
    Input(array,n)
    print(array)
    key=int(input("Enter key:"))
    start=timeit.default_timer()
    s= binary_search(array,key)
    print("element found------",s)
    times=timeit.default_timer()-start
    N.append(n)
    CPU.append(round(float(times)*1000000,2))
print("N CPU")
for t in range(0,trail):
    print(N[t],CPU[t])
    plt.plot(N,CPU)
    plt.scatter(N,CPU,color="red",marker="*",s=50)
    plt.xlabel("array size- N")
    plt.ylabel=("CPU Processing Time")
    plt.title("binary search time efficiency")
    plt.show()