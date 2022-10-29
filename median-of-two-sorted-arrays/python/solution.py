INT_MAX = float("infinity")
INT_MIN = -INT_MAX

PYTHON_EFFICIENCY_CUTOFF = 350

def bad_solution(nums1: list[int], nums2: list[int]) -> float:
    lengths_combined = len(nums1) + len(nums2)
    sorted_lists = sorted(nums1 + nums2)
    if lengths_combined % 2:
        return sorted_lists[(lengths_combined - 1) // 2]
    return (sorted_lists[lengths_combined // 2] + sorted_lists[(lengths_combined - 1) // 2]) / 2

def median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """O(log(min(m, n))) solution.
    
    This solution is actually the "best" runtime solution, but since the runtime
    coefficient in python is so high, on leetcode, this solution will have a higher "faster than x%":

    ```py
    def bad_solution(nums1: list[int], nums2: list[int]) -> float:
        lengths_combined = len(nums1) + len(nums2)
        sorted_lists = sorted(nums1 + nums2)
        if lengths_combined % 2:
            return sorted_lists[(lengths_combined - 1) // 2]
        return (sorted_lists[lengths_combined // 2] + sorted_lists[(lengths_combined - 1) // 2]) / 2
    ```

    The reason why the code above is faster, despite the O(n+m*log(n+m)) runtime, is because `sorted`
    is implemented in C, which has a much lower coefficient. Once you start throwing a few thousand
    elements at either, this solution will beat the other one. A merge sort implemented in C
    might beat this though.
    """
    shorter_list = nums1 if len(nums1) < len(nums2) else nums2
    longer_list = nums2 if len(nums1) < len(nums2) else nums1

    shorter_length = len(shorter_list)
    longer_length = len(longer_list)

    # Check if the input is valid
    if not shorter_list and not longer_list:
        raise ValueError("No data provided")
    elif not shorter_list:
        if longer_length % 2:
            return longer_list[(longer_length - 1) // 2]
        return (longer_list[longer_length // 2] + longer_list[(longer_length - 1) // 2]) / 2

    low_index = 0
    high_index = shorter_length * 2

    while (low_index <= high_index):
        shorter_list_cutpoint = (low_index + high_index) // 2
        longer_list_cutpoint =  shorter_length + longer_length - shorter_list_cutpoint

        long_list_left = INT_MIN if longer_list_cutpoint == 0 else longer_list[(longer_list_cutpoint - 1) // 2]
        short_list_left = INT_MIN if shorter_list_cutpoint == 0 else shorter_list[(shorter_list_cutpoint - 1) // 2]

        long_list_right = INT_MAX if longer_list_cutpoint == longer_length * 2 else longer_list[longer_list_cutpoint // 2]
        short_list_right = INT_MAX if shorter_list_cutpoint == shorter_length * 2 else shorter_list[shorter_list_cutpoint // 2]

        # A more intuitive way to think of this is:
        # if long_list_left <= short_list_right and short_list_left <= long_list_right:
        #   return (max(long_list_left, short_list_left) + min(long_list_right, short_list_right)) / 2

        if long_list_left > short_list_right:
            low_index = shorter_list_cutpoint + 1
        elif short_list_left > long_list_right:
            high_index = shorter_list_cutpoint - 1
        else:
            return (max(long_list_left, short_list_left) + min(long_list_right, short_list_right)) / 2

    raise ValueError("Not Found")
        

import time

N = 10000

a = list(range(20))
b = list(range(N, N*2))

print(len(a) + len(b))

start_good = time.time()
median_of_two_sorted_arrays(a, b)
end_good = time.time()

start_bad = time.time()
bad_solution(a, b)
end_bad = time.time()

print("good", end_good - start_good)
print("bad", end_bad - start_bad)

if (end_good - start_good) > (end_bad - start_bad):
    print("sorted still faster")


