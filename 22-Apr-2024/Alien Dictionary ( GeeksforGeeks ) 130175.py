# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        letters = set()
        
        for i in range(N-1):
            ptr1, ptr2 = 0, 0
            while ptr1 < len(alien_dict[i]) and ptr2 < len(alien_dict[i+1]):
                if ptr1 >= 1 and alien_dict[i][ptr1-1] != alien_dict[i+1][ptr2-1]:
                    break
                elif alien_dict[i][ptr1] != alien_dict[i+1][ptr2]:
                    graph[alien_dict[i][ptr1]].append(alien_dict[i+1][ptr2])
                    indegree[alien_dict[i+1][ptr2]] += 1

                letters.add(alien_dict[i][ptr1])
                letters.add(alien_dict[i+1][ptr1])
                
                ptr1 += 1
                ptr2 += 1
        
            while ptr1 < len(alien_dict[i]):
                letters.add(alien_dict[i][ptr1])
                ptr1 += 1
            while ptr2 < len(alien_dict[i+1]):
                letters.add(alien_dict[i+1][ptr2])
                ptr2 += 1    


        queue = deque()

        for letter in letters:
            if not indegree[letter]:
                queue.append(letter)
                
        order = []       
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for ngb in graph[curr]:
                indegree[ngb] -= 1
                if indegree[ngb] == 0:
                    queue.append(ngb)
                    
   
        return ''.join(order)
                
                
                    
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends