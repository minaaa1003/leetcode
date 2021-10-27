#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return node
        #using map to create 1-1 copies
        map_ = {}
        #create new copies for each node
        self.copyNode(node, map_)
        #connect new neighbors to new nodes
        self.copyNeighbors(node, map_, set())
        return map_[node]
        
    def copyNode(self, node, map_):
        if node in map_: return
        #key: old node; value: new node and its neighbors
        newNode = Node(node.val,[])
        map_[node] = newNode
        #loop through the neighbors of each node 
        for n in (node.neighbors):
            self.copyNode(n,map_)
        
    def copyNeighbors(self, node, map_, visited=set()):
        if node in visited:
            return
        visited.add(node)
    
        for n in (node.neighbors):
            map_[node].neighbors.append(map_[n])
            self.copyNeighbors(n, map_, visited)
        
        
# @lc code=end

