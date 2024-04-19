# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        # cnt = dict(sorted(cnt.items(), key=lambda x: x[0]))

        _cnt = []
        for word, c in cnt.items():
            _cnt.append((-c, word))
        heapq.heapify(_cnt)    
        print(_cnt) 
        ans = []   
        for _ in range(k):
            c, word = heapq.heappop(_cnt)
            ans.append(word)
        return ans    


        