class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)
    
    def build(self, data, node, start, end):
        # end case if the start is equal to the end of the node
        if start == end:
            # eqal to the start element of the bt
            self.tree[node] = [data[start]]  
            return      
        
        # if not check for the next element in the tree (childs)
        # calculate the mid
        mid = (start + end) // 2
        
        # recursively build the child trees
        self.build(data,2*node + 1, start, mid)
        self.build(data,2*node + 2, mid+1, end)
        
        # after building merge them to the current node
        self.tree[node] = sorted(self.tree[2*node + 1] + self.tree[2*node + 2])
        
if __name__ == "__main__":
    segmentTree = SegmentTree([4, 3, 2, 5, 1])
    print(segmentTree.tree)