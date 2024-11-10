def fractionalKnapsack(w, items):
    # Sort items based on profit-to-weight ratio in descending order
    items.sort(key=lambda x: x['profit'] / x['weight'], reverse=True)
    
    finalValue = 0.0
    for item in items:
        if w >= item['weight']:
            finalValue += item['profit']
            w -= item['weight']
        else:
            finalValue += item['profit'] * (w / item['weight'])
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    items = []
    for i in range(n):
        profit = int(input(f"Enter profit of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        items.append({'profit': profit, 'weight': weight})
    
    w = int(input("Enter capacity of knapsack: "))
    print("Maximum value in knapsack:", fractionalKnapsack(w, items))


































"""def fractionalKnapsack(w, items):
Defines a function fractionalKnapsack that takes two parameters:
w: The maximum weight (capacity) the knapsack can carry.
items: A list of dictionaries where each dictionary represents an item with profit and weight keys.
Sorting Items by Profit-to-Weight Ratio
python

Copy code
    items.sort(key=lambda x: x['profit'] / x['weight'], reverse=True)
This line sorts items based on each item's profit-to-weight ratio in descending order.
key=lambda x: x['profit'] / x['weight']: The lambda function calculates the profit-to-weight ratio for each item, which helps prioritize items with a higher profit per unit weight.
reverse=True: This sorts items from highest to lowest ratio, ensuring that the most valuable items (by ratio) are considered first.
Initializing the Final Value
python

Copy code
    finalValue = 0.0
Initializes finalValue to 0.0, which will store the total profit as items are added to the knapsack.
Looping Through the Sorted Items
python

Copy code
    for item in items:
This line starts a for loop that iterates over each item in the items list, in the sorted order (highest profit-to-weight ratio first).
Adding Full Items
python

Copy code
        if w >= item['weight']:
            finalValue += item['profit']
            w -= item['weight']
if w >= item['weight']: Checks if the remaining weight capacity w is enough to take the entire item.
finalValue += item['profit']: Adds the full profit of the item to finalValue since we’re taking the whole item.
w -= item['weight']: Subtracts the weight of the item from the remaining capacity w, updating it for the next iteration.
Adding Fractional Items
python

Copy code
        else:
            finalValue += item['profit'] * (w / item['weight'])
            break
else: If there isn’t enough remaining capacity to take the whole item, we take only part of it.
finalValue += item['profit'] * (w / item['weight']): Adds a fraction of the item’s profit to finalValue, based on the remaining capacity w as a proportion of the item’s weight.
break: Stops the loop because the knapsack is now full.
Returning the Result
python

Copy code
    return finalValue
Returns the total profit finalValue that can be achieved with the given knapsack capacity.
Main Code Block (User Input and Function Call)
python

Copy code
if __name__ == "__main__":
This line ensures that the code within this block only runs if the script is executed directly, not if it’s imported as a module.
Getting Input for Items
python

Copy code
    n = int(input("Enter number of items: "))
    items = []
n: Asks the user for the number of items and stores it in n.
items = []: Initializes an empty list to store each item’s profit and weight as dictionaries.
python

Copy code
    for i in range(n):
        profit = int(input(f"Enter profit of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        items.append({'profit': profit, 'weight': weight})
This loop iterates n times to collect the profit and weight of each item.
profit and weight are collected as integers from user input.
A dictionary representing the item (with keys profit and weight) is appended to the items list.
Getting Knapsack Capacity and Calculating the Result
python

Copy code
    w = int(input("Enter capacity of knapsack: "))
    print("Maximum value in knapsack:", fractionalKnapsack(w, items))
w: Asks the user for the knapsack’s weight capacity and stores it in w.
Calls fractionalKnapsack(w, items) with the knapsack capacity w and the list of items, then prints the maximum achievable profit in the knapsack."""