################################################################################
# Prefix Reversal Sorting
#
# Name: Luis Guillot Lozano 
#
# Please use this comment section to list any references or sources you used
# to complete the assignment.
# 
# List of references:
#   - Pancake Sorting Algorithm (Wikipedia)
#   - Python list slicing documentation
# 
################################################################################

################################################################################
# Required functions. DO NOT MODIFY THESE FUNCTION DECLARATIONS.
# Replace the body of each function with your implementation
################################################################################

# Algorithm for sorting an arbitrary list using prefix reversals.
# INPUT: arr, a list of integers
# OUTPUT: a sequence of prefix indices that sort arr
def pr_general_sort(arr: list[int]) -> list[int]:
    """
    Sort any array using the pancake sort algorithm.
    
    Strategy: Find the largest unsorted element, flip it to the front,
    then flip it to its correct position. Repeat for remaining elements.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    
    # Process array from largest to smallest position
    for curr_size in range(n, 1, -1):
        # Find index of maximum element in unsorted portion
        max_idx = 0
        for i in range(curr_size):
            if work_arr[i] > work_arr[max_idx]:
                max_idx = i
        
        # If max is already in correct position, skip
        if max_idx == curr_size - 1:
            continue
            
        # Step 1: Flip max element to front (if not already there)
        if max_idx != 0:
            reversals.append(max_idx)
            work_arr = work_arr[:max_idx+1][::-1] + work_arr[max_idx+1:]
        
        # Step 2: Flip max element to its correct position
        reversals.append(curr_size - 1)
        work_arr = work_arr[:curr_size][::-1] + work_arr[curr_size:]
    
    return reversals


# Algorithm for sorting a tritonic list using prefix reversals.
# INPUT: arr, a list of integers, assumed to be tritonic
# OUTPUT: a sequence of prefix indices that sort arr
def pr_tritonic_sort(arr: list[int]) -> list[int]:
    """
    Sort a tritonic array.
    
    Strategy: Use general pancake sort, which works for all inputs
    including tritonic arrays.
    """
    return pr_general_sort(arr)


# Algorithm for sorting a binary list using prefix reversals.
# INPUT: arr, a list of binary (0 or 1) values
# OUTPUT: a sequence of prefix that sort arr
def pr_binary_sort(arr: list[int]) -> list[int]:
    """
    Sort a binary array using pancake sort adapted for binary values.
    
    Strategy: Move largest values (1s) to their correct positions.
    Since we only have 0s and 1s, we sort by moving 1s to the back.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    
    # Count how many 1s there are - they go at the end
    num_ones = work_arr.count(1)
    
    # We need to place 1s in positions from (n - num_ones) to (n-1)
    # Work backwards from the last position
    for curr_pos in range(n - 1, n - num_ones - 1, -1):
        # If this position already has a 1, skip it
        if work_arr[curr_pos] == 1:
            continue
        
        # Find a 1 before curr_pos
        one_idx = -1
        for i in range(curr_pos):
            if work_arr[i] == 1:
                one_idx = i
                break
        
        if one_idx == -1:
            # No more 1s to move
            break
        
        # Move this 1 to curr_pos using two flips
        # First flip: bring 1 to position 0
        if one_idx > 0:
            reversals.append(one_idx)
            work_arr = work_arr[:one_idx+1][::-1] + work_arr[one_idx+1:]
        
        # Second flip: move 1 from position 0 to curr_pos
        reversals.append(curr_pos)
        work_arr = work_arr[:curr_pos+1][::-1] + work_arr[curr_pos+1:]
    
    return reversals


# Algorithm for sorting a ternary list using prefix reversals.
# INPUT: arr, a list of ternary (0, 1, or 2) values
# OUTPUT: a sequence of prefix indices that sort arr
def pr_ternary_sort(arr: list[int]) -> list[int]:
    """
    Sort a ternary array using modified pancake sort.
    
    Strategy: First place all 2s at the back, then place all 1s in the middle.
    0s naturally end up at the front.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    
    # Count each value
    num_twos = work_arr.count(2)
    num_ones = work_arr.count(1)
    
    # Phase 1: Place all 2s at the end (positions n-num_twos to n-1)
    for curr_pos in range(n - 1, n - num_twos - 1, -1):
        if work_arr[curr_pos] == 2:
            continue
        
        # Find a 2 before curr_pos
        two_idx = -1
        for i in range(curr_pos):
            if work_arr[i] == 2:
                two_idx = i
                break
        
        if two_idx == -1:
            break
        
        # Move this 2 to curr_pos
        if two_idx > 0:
            reversals.append(two_idx)
            work_arr = work_arr[:two_idx+1][::-1] + work_arr[two_idx+1:]
        
        reversals.append(curr_pos)
        work_arr = work_arr[:curr_pos+1][::-1] + work_arr[curr_pos+1:]
    
    # Phase 2: Place all 1s in the middle (positions n-num_twos-num_ones to n-num_twos-1)
    for curr_pos in range(n - num_twos - 1, n - num_twos - num_ones - 1, -1):
        if work_arr[curr_pos] == 1:
            continue
        
        # Find a 1 before curr_pos
        one_idx = -1
        for i in range(curr_pos):
            if work_arr[i] == 1:
                one_idx = i
                break
        
        if one_idx == -1:
            break
        
        # Move this 1 to curr_pos
        if one_idx > 0:
            reversals.append(one_idx)
            work_arr = work_arr[:one_idx+1][::-1] + work_arr[one_idx+1:]
        
        reversals.append(curr_pos)
        work_arr = work_arr[:curr_pos+1][::-1] + work_arr[curr_pos+1:]
    
    return reversals


################################################################################
# HELPER FUNCTIONS
# put any auxiliary function definitions below here
################################################################################

def apply_reversal(arr: list[int], index: int) -> list[int]:
    """Apply a prefix reversal at the given index."""
    return arr[:index+1][::-1] + arr[index+1:]

def find_max_index(arr: list[int], end: int) -> int:
    """Find the index of the maximum element in arr[0:end]."""
    max_idx = 0
    for i in range(end):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx
