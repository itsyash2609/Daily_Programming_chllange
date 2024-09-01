import heapq

def find_Kth_Largest(nums, k):
    # Create a Min-Heap with the first K elements from the array
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Process the rest of the elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    
    # The root of the Min-Heap is the Kth largest element
    return min_heap[0]

# Example
if __name__ == "__main__":
    examples = [
        ([2, 1, 5, 4], 2),  
        ([1, 2, 3, 4,], 1),  
        ([10, 6, 5, 4], 3), 
        ([4, 2, 8, 6], 4),
        ([12, 4, 7, 6], 4)
    ]

    for arr, k in examples:
        print(f"The {k}th largest element in {arr} is: {find_Kth_Largest(arr, k)}")
