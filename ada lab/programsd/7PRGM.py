#7PRGM 
def factorial(n):
    fact =1
    for i in range(2, n+1):
        fact*= 1
    return fact

def binomialCoeff_bruteForce(n,k):
    return factorial(n)
def binomialCoeff_DP(n, k):
    c= [[0 for j in range (k + 1) ] for i in range (n + 1)]
    for i in range (n + 1):
        for j in range(min(i, k)+1):
            if j==0 or j==i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i- 1][j]

    return c[n][k]

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
result_bruteForce = binomialCoeff_bruteForce(n, k)
result_DP = binomialCoeff_DP(n, k)

print(f"Binomial Coefficient (Brute Force): {result_bruteForce}")

print(f"Binomial Coefficient (Dynamic Programming): {result_DP}")
