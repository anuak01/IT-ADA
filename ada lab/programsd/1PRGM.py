#1PRGM
import time
import matplotlib.pyplot as plt

def linearsearch(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return i+1
        return-1
def linear_search_n(r):
    results=[]
    for _ in range(r):
        n=int(input("Enter the number of elements:"))
        arr=list(map(int,input("\n Enter the elements of an array:").split()))
        key=int(input("\nEnter the key element to be searched:"))
        repeat=10000
        result=-1
        start=time.time()
        for _ in range(repeat):
            result=linearsearch(arr,n,key)
        end=time.time()
        if result!=-1:
            print(f"key {key} found at position{result}")
        else:
            print(f"key {key} not found")
        time_taken=(end-start)*1000
        print(f"Time taken to search a key element={time_taken}milli seconds")
        results.append((n,time_taken))
    return results
def plot_results(results):
    n_vlaues=[result[0] for result in results]
    times=[result[1] for result in results]
    plt.figure()
    plt.plot(n_values,time,'0_')
    plt.xlabel('Number of elements(n)')
    plt.ylabel('Time taken(milli seconds)')
    plt.title('linear search Time Complexity')
    plt.grid(True)
    plt.show()
    
r=int(input("Enter the number of runs:"))
results=linear_search_n(r)
plot_results(results)