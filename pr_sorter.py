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
    Optimized general sort with better skipping logic.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    
    for curr_size in range(n, 1, -1):
        # Find maximum in unsorted portion
        max_idx = 0
        max_val = work_arr[0]
        
        for i in range(1, curr_size):
            if work_arr[i] > max_val:
                max_val = work_arr[i]
                max_idx = i
        
        # Skip if already in correct position
        if max_idx == curr_size - 1:
            continue
        
        # Two-flip technique
        if max_idx > 0:
            reversals.append(max_idx)
            work_arr = work_arr[:max_idx+1][::-1] + work_arr[max_idx+1:]
        
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
    Optimized binary sort - search backwards for closest elements.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    num_ones = work_arr.count(1)
    
    # Place 1s at the end, working backwards
    for curr_pos in range(n - 1, n - num_ones - 1, -1):
        # Skip if already has a 1
        if work_arr[curr_pos] == 1:
            continue
        
        # Search BACKWARDS for the closest 1
        one_idx = -1
        for i in range(curr_pos - 1, -1, -1):  # KEY CHANGE: backwards search
            if work_arr[i] == 1:
                one_idx = i
                break
        
        if one_idx == -1:
            break
        
        # Two-flip technique
        if one_idx > 0:
            reversals.append(one_idx)
            work_arr = work_arr[:one_idx+1][::-1] + work_arr[one_idx+1:]
        
        reversals.append(curr_pos)
        work_arr = work_arr[:curr_pos+1][::-1] + work_arr[curr_pos+1:]
    
    return reversals


# Algorithm for sorting a ternary list using prefix reversals.
# INPUT: arr, a list of ternary (0, 1, or 2) values
# OUTPUT: a sequence of prefix indices that sort arr
def pr_ternary_sort(arr: list[int]) -> list[int]:
    """
    Optimized ternary sort - search backwards for closest elements.
    """
    reversals = []
    work_arr = arr.copy()
    n = len(work_arr)
    num_twos = work_arr.count(2)
    num_ones = work_arr.count(1)
    
    # Phase 1: Place all 2s at the end
    for curr_pos in range(n - 1, n - num_twos - 1, -1):
        if work_arr[curr_pos] == 2:
            continue
        
        # Search BACKWARDS for closest 2
        two_idx = -1
        for i in range(curr_pos - 1, -1, -1):  # KEY CHANGE: backwards
            if work_arr[i] == 2:
                two_idx = i
                break
        
        if two_idx == -1:
            break
        
        if two_idx > 0:
            reversals.append(two_idx)
            work_arr = work_arr[:two_idx+1][::-1] + work_arr[two_idx+1:]
        
        reversals.append(curr_pos)
        work_arr = work_arr[:curr_pos+1][::-1] + work_arr[curr_pos+1:]
    
    # Phase 2: Place all 1s in the middle
    for curr_pos in range(n - num_twos - 1, n - num_twos - num_ones - 1, -1):
        if work_arr[curr_pos] == 1:
            continue
        
        # Search BACKWARDS for closest 1
        one_idx = -1
        for i in range(curr_pos - 1, -1, -1):  # KEY CHANGE: backwards
            if work_arr[i] == 1:
                one_idx = i
                break
        
        if one_idx == -1:
            break
        
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
