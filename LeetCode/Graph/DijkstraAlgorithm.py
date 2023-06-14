"""
Question
https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=eventual-safe-states
"""

#Approach
"""
#Approach 1: Using Queue
--> This is the most basic approach
--> We will be storing the pairs of (node, dist) in the queue
--> We have to process each pair by traversing thorugh it's neighbour and finding a new shortest path

#Approach 2: Using Heap
--> The previous approach can be optimised and made faster by using a heap since heap
--> We can store the pairs pairs (dist, node) in the min-heap.
--> The pair with the smallest dist will be on top of heap and processed first
--> So the shortest path will be processing first and we would not need to process many longer paths that we were
doing in the queue approach

#Approach 3: Using SortedSet
--> There is another approach using SortedSet
--> In this approach we can change the dist array as soon as we enter into set
--> If we find a better path then we will delete the previous path from the set(if present)
--> It will take advantage of the heap also i.e. smaller dist to process first
--> We can't say if SortedSet has a better time complexity than heap, time complexity wise both are same.
Depending on the graph type one will run faster than another  

"""

#Code
#Approach 1: Heap
import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        INF = 10 ** 20
        dist = [INF] * V
        h = []
        heapq.heappush(h, (S, 0))
        while h:
            node, currDist = heapq.heappop(h)
            if currDist < dist[node]:
                #found a new shorter path
                dist[node] = currDist
                for nextNode, nextDist in adj[node]:
                    if dist[nextNode] > currDist + nextDist:
                        heapq.heappush(h, (nextNode, currDist + nextDist))
        return dist 

#Approach 2: SortedSet
from sortedcontainers import SortedSet
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        INF = 10 ** 20
        dist = [INF] * V
        st = SortedSet()
        st.add((0, S))
        dist[S] = 0
        
        while len(st) > 0:
            currDist, node = st.pop(0)
            for nextNode, nextDist in adj[node]:
                if nextDist + currDist < dist[nextNode]:
                    st.discard((dist[nextNode], nextNode))
                    st.add((currDist + nextDist, nextNode))
                    #Here we are modifying the dist arr while adding to the set
                    #In heap we didn't need to use this either way it would have worked
                    #Here in order to use the SortedSet and delete the previous longer paths which are not processed
                    #we have to modify the dist arr when the pair is added to the SortedSet
                    dist[nextNode] = currDist + nextDist
        return dist
