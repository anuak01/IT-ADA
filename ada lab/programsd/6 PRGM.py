#6 PRGM 
import timeit
import random
import matplotlib.pyplot as plt
def Input(array,n):
    for i in range(0,n):
        ele=random.randrange(1,50)
        array.append(ele)
def partition(array,low,high):
    i=(low-1)
    pivot=array[high]
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)
def quickSort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)
N=[]
CPU=[]
trail=int(input("Enter no.of trails:"))
for t in range(0,trail):
    array=[]
    print("---->Trail No.:",t+1)
    n=int(input("Enter number of elements:"))
    Input(array,n)
    start=timeit.default_timer()
    quickSort(array,0,n-1)
    times=timeit.default_timer()-start
    print("Sorted Array:")
    print(array)
    N.append(n)
    CPU.append(round(float(times)*1000000,2))
print("N,CPU")
for t in range(0,trail):
    print(N[t],CPU[t])
    
plt.plot(N,CPU)
plt.scatter(N,CPU,color="red",marker="*",s=50)
plt.xlabel('array size - N')
plt.ylabel('CPU Processing Time')
plt.title('Quick Sort Time Efiiciency')
plt.show()