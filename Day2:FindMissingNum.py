def find_missing_number(arr):
  """
  Args:
    arr: A list of integers, where one integer is missing from the range 1 to n.

  Returns:
    The missing integer.
  """

  n = len(arr) + 1
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(arr)

  return expected_sum - actual_sum

# Example usage:
arr = [1, 2, 3, 5]
missing_number = find_missing_number(arr)
print("Missing Number:", missing_number)
