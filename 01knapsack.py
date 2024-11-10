def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = 3
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    max_value, selected_items = knapsack_01(n, values, weights, W)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """def knapsack_01(n, values, weights, W):
This defines a function knapsack_01 that takes four parameters:
n: The number of items.
values: A list containing the value of each item.
weights: A list containing the weight of each item.
W: The maximum weight the knapsack can carry.
python

Copy code
    dp = [[0] * (W+1) for _ in range(n+1)]
Initializes a 2D list dp with dimensions (n+1) x (W+1). This table will store the maximum value achievable with i items and w weight capacity.
Each cell dp[i][w] represents the maximum value achievable with the first i items and a knapsack capacity of w.
python

Copy code
    for i in range(n+1):
        for w in range(W+1):
These nested loops iterate over each item (i) and each weight capacity (w) to fill up the dp table.
python

Copy code
            if i == 0 or w == 0:
                dp[i][w] = 0
Base condition: If there are 0 items (i == 0) or the knapsack capacity is 0 (w == 0), the maximum value is 0, so dp[i][w] is set to 0.
python

Copy code
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
If the current item can fit in the knapsack (weights[i-1] <= w), there are two choices:
Exclude the item, keeping the maximum value from the previous row: dp[i-1][w].
Include the item, adding its value to the maximum value achievable with the remaining weight (w - weights[i-1]): dp[i-1][w-weights[i-1]] + values[i-1].
The cell dp[i][w] is set to the maximum of these two options.
python

Copy code
            else:
                dp[i][w] = dp[i-1][w]
If the item’s weight exceeds the current capacity (weights[i-1] > w), the item cannot be included. Thus, dp[i][w] is set to the maximum value achievable without this item (dp[i-1][w]).
python

Copy code
    selected_items = []
    i, w = n, W
Initializes selected_items as an empty list to store the indices of the selected items.
Sets i and w to start at the last item (n) and the full capacity (W) to trace back the items included in the solution.
python

Copy code
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
Traces back through the dp table to determine which items were included in the optimal solution:
If dp[i][w] != dp[i-1][w], the current item (i-1) was included, so it’s added to selected_items.
The capacity w is reduced by the weight of the included item.
pyth

Copy code
        i -= 1
Moves to the previous item to continue tracing back.
puddle

Copy code
    return dp[n][W], selected_items

``
Returns the maximum value (dp[n][W]) and the list of selected item indices.
py

Copy code
if __name__ == "__main__":

``
This line starts the main script, which will only run if the script is executed directly (not imported as a module).
python

Copy code
    n = 3
    values = [60, 100, 120]
    weights = [
   
10, 20, 30]
    W = 50

``
Initializes the number of items (n), their values, weights, and the maximum knapsack weight (W).
python

Copy code
    max_value, selected_items = knapsack_01(n, values, weights, W)
Calls the knapsack_01 function with the above inputs and stores the results in max_valueaselected_items.
python

Copy code
    print("Maximum value:", max_value)
    
    p

 
print("Selected items:", selected_items)
Prints the maximum value that can be obtained and the list of selected items (by their indices)."""