def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
    
    Returns:
        The sorted list (modifies in-place and returns)
    """
    # Start from the second element (index 1) since first element is already "sorted"
    for i in range(1, len(arr)):
        # Store the current element we want to insert into sorted portion
        key = arr[i]
        
        # Start comparing from the element just before current position
        j = i - 1
        
        # Move elements greater than key one position ahead
        # This creates space for inserting the key at correct position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move to the previous element
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


# Example usage with step-by-step visualization
def insertion_sort_verbose(arr):
    """
    Insertion sort with detailed printing of each step.
    Great for learning and understanding the algorithm.
    """
    print(f"Original array: {arr}")
    print("-" * 50)
    print("Start sort from the second element (index 1). Because the first element is trivially sorted.")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"\nStep {i}: Inserting {key}")
        print(f"Sorted portion: {arr[:i]}")
        print(f"Current array : {arr}")
        
        # Track number of shifts
        shifts = 0
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            print(f"  Shift {arr[j]} from index {j} to {j+1} because it's greater than current inserting element: {key}")
            j -= 1
        
        arr[j + 1] = key
        print(f"  Insert {key} at index {j+1}")
        
        if shifts == 0:
            print(f"  {key} was already in correct position!")
        
        print(f"After step {i}: {arr}")
    
    print("\n" + "=" * 50)
    print(f"Final sorted array: {arr}")
    return arr


# Test the algorithm
if __name__ == "__main__":
    # Example 1: Basic sort
    numbers = [5, 2, 4, 6, 1, 3]
    print("EXAMPLE 1: Basic Insertion Sort")
    print("=" * 50)
    result = insertion_sort(numbers.copy())
    print(f"Input:  {[5, 2, 4, 6, 1, 3]}")
    print(f"Output: {result}\n")
    
    # Example 2: Verbose sort to see each step
    print("\nEXAMPLE 2: Step-by-Step Visualization")
    print("=" * 50)
    numbers2 = [5, 2, 4, 6, 1, 3]
    insertion_sort_verbose(numbers2)
    
    # Example 3: Already sorted array
    print("\n\nEXAMPLE 3: Already Sorted Array")
    print("=" * 50)
    sorted_arr = [1, 2, 3, 4, 5]
    insertion_sort_verbose(sorted_arr)
    
    # Example 4: Reverse sorted array (worst case)
    print("\n\nEXAMPLE 4: Reverse Sorted (Worst Case)")
    print("=" * 50)
    reverse_arr = [5, 4, 3, 2, 1]
    insertion_sort_verbose(reverse_arr)