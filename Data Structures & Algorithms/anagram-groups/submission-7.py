class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        dict2 = {}

        res = []

        for i, j in enumerate(strs):
            dict1[i] = [''.join(map(str, sorted([ord(x) for x in j]))), j]

        for i in dict1.values():
            if i[0] not in dict2.keys():
                dict2[i[0]] = [i[1]]
            else:
                dict2[i[0]].append(i[1])

        for val in dict2.values():
            res.append(val)
        return res