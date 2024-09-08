class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:


        # dict of positions of items in arr2, or default to high value
        arr2_position = defaultdict(lambda: 10**10)
        for i, n in enumerate(arr2):
            arr2_position[n] = i

        return sorted(arr1, key=lambda x: (arr2_position[x], x))
