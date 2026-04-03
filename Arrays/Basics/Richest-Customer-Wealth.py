'''
You are given an m×n integer grid accounts where accounts[i][j] is the amount the i-th customer has in the j-th bank. 
Return the wealth of the richest customer (max row sum).

Example 1

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation: Both customers have wealth 6.
'''

def maximum_wealth(accounts):
    return max(sum(customer) for customer in accounts)

accounts = [[1,5],[7,3],[3,5]]
print(maximum_wealth(accounts))