################################################################################
# Prefix Reversal Sorting
#
# Name: Luis Guillot Lozano 
#
# Please use this comment section to list any references or sources you used
# to complete the assignment.
# 
# List of references:
#   - 
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
    Sort a tritonic array (increasing-decreasing-increasing pattern).
    
    For now, using general sort. Will optimize later.
    """
    return pr_general_sort(arr)


# Algorithm for sorting a binary list using prefix reversals.
# INPUT: arr, a list of binary (0 or 1) values
# OUTPUT: a sequence of prefix that sort arr
def pr_binary_sort(arr: list[int]) -> list[int]:
    """
    Sort an array containing only 0s and 1s.
    
    For now, using general sort. Will optimize later.
    """
    return pr_general_sort(arr)


# Algorithm for sorting a binary list using prefix reversals.
# INPUT: arr, a list of ternary (0, 1, or 2) values
# OUTPUT: a sequence of prefix indices that sort arr
def pr_ternary_sort(arr: list[int]) -> list[int]:
    """
    Sort an array containing only 0s, 1s, and 2s.
    
    For now, using general sort. Will optimize later.
    """
    return pr_general_sort(arr)


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

