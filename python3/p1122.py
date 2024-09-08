class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:


        arr2_position = {}
        for i, n in enumerate(arr2):
            arr2_position[n] = i

        @staticmethod
        def keym(x):
            if x in arr2_position:
                return arr2_position[x]
            return x

        arr1_set = set(arr1)
        arr2_set = set(arr2)

        arr1_uniq = []
        for n in arr1:
            if n not in arr2_set:
                arr1_uniq.append(n)
        arr1_uniq.sort()

        common = []
        for n in arr1:
            if n in arr2_set:
                common.append(n)
        common.sort(key=keym)

        return common + arr1_uniq
