def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the maximum candies among all kids
    return [candy + extraCandies >= max_candies for candy in candies]

# Example test cases
print(kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
