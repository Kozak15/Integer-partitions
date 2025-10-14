
#Find the number of ways to partition n using integers up to k, about O(2*n) time complexity
#Decreasable to O(n*k) using memoization or dynamic programming
def parts(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return parts(n, k-1) + parts(n-k, k)
#Partition n using exactly k parts, assuming n>=k
def partition_largest(n, k):
  if k == 1 or k == n:
    return 1
  else:
    return parts(n, k) - parts(n, k-1)
#Partition n using exactly k parts (alternative method)
def partition_kparts(n, k):
    if n == 0 and k == 0:
        return 1
    if n <= 0 or k <= 0:
        return 0
    return partition_kparts(n-1 , k-1) + partition_kparts(n-k, k)
#Partition n into distinct parts
def count_partitions_max(n, max_part):
    if n == 0:
        return 1
    if n < 0 or max_part == 0:
        return 0
    return count_partitions(n, max_part - 1) + count_partitions(n - max_part, max_part - 1)
#Partition n into distinct parts (wrapper function)
def partition_distinct(n):
    return count_partitions(n,n)
#Partition n into odd parts, equivalent to partition into distinct parts    
def partition_odd_dp(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for odd in range(1, n+1, 2):
        for s in range(odd, n+1):
            dp[s] += dp[s-odd]
    return dp[n]
#Pentagonal number theorem helper functions
def a(n):
    return (n + 1) * (3*n + 2)//2
def b(n):
    return (n + 1) * (3*n + 4)//2
#Partition n using pentagonal number theorem
def p(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n <= 3:
        return n
    else:
        num_lst,sgn_lst,num,index,count = [],[],0,0,0
        while True:
            x, y = a(num), b(num)
            if x > n and y > n:
                break
            if x <= n:
                num_lst.append(x)
            if y <= n:
                num_lst.append(y)
            num += 1
        num_lst.sort()
        for i in range(len(num_lst)//4):
            sgn_lst.extend(['+', '+', '-', '-'])
        sgn_lst.extend(['+', '+', '-', '-'][:len(num_lst)%4])
        for item in sgn_lst:
            val = num_lst[index]
            if item == '+':
                count += p(n - val)
            else:
                count -= p(n - val)
            index += 1
        return count


