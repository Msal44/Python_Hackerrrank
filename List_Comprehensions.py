
#This is where we receive the data. (this part is provided by hackerrank)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
'''    
with list comprehension we create a new list. i, j, k will be our output values which given from out input x, y, z. We want to avoid i + j + k having the sum of 3. 

Notice in the sample output below how array of elements within the list, each do not sum up to 3.
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


create a new list, [i,j,k] is responsible for creating a new list of each combination of values. We create a loop with a range and the if state,etm state the sum should not equal 3.
''' 

new_list = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k !=n]
    
print(new_list)
