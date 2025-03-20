def flatten_list(arr):
    result=[]
    for item in arr:
        if isinstance(item,list):
            result.extend(flatten_list(item))  # Recursively flatten nested lists
        else:
            result.append(item)  # Add non-list elements directly
    return result
arr=[1, [2, [3, [4, 5]], 6], 7]
flattened=flatten_list(arr)
print(flattened)
