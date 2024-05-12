from collections import defaultdict
def merge_arrays(nums1, nums2):
    d1 = defaultdict(int, {a: b for a, b in nums1})
    d2 = defaultdict(int, {a: b for a, b in nums2})    
    merged = []
    for k in sorted(set(d1.keys()).union(set(d2.keys()))):
        merged.append([k, d1[k] + d2[k]])    
    return merged
def test_merge_arrays():
    nums1 = [(1, 2), (2, 3), (3, 4)]
    nums2 = [(2, 5), (3, 6), (4, 7)]    
    merged = merge_arrays(nums1, nums2)
    print("Merged array:", merged)
test_merge_arrays()

