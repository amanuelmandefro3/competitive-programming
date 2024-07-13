# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        strs_group = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            strs_group[key].append(word)



        return list(strs_group.values()) 