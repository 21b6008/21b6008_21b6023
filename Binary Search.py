class BinarySearchNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def add_child (self, data): ## method to add a child to the tree
        if data == self.data:
            return # node already exists
        
        if data < self.data:
            ##add to the left subtree
            if self.left:
                ##keep going down into left tree to end
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)
        else:
            ##add it to right subtree
            if self.right:
                ##keep going down into right tree to end
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)

    def in_order_traversal(self): # traverses the tree in in_order method
        elements =[]
        ## visit the left subtree .. visit means add to the elements array
        if self.left:
            elements += self.left.in_order_traversal()

        ## visit the node
        elements.append(self.data)

        ## visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search(self, val):
        if val == self.data:
            return True
        
        if val < self.data: # vlaue might be in left subtree
            if self.left: # if left subtree exists
                return self.left.search(val) # search within left subtree and return the result
            else: ## no left subtree
                return False # not found

        if val > self.data: # vlaue might be in right subtree
            if self.right: # if right subtree exists
                return self.right.search(val) # search within right subtree and return the result
            else: ## no right subtree
                return False # not found   

    def find_max(self): ## this is our method to find the maximum value in the subtree
        if self.right is None:
            return self.data
        return self.right.find_max() # could do this in a while loop also

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min() # could do this in a while loop also
        
    def delete(self, val):
        if val < self.data:
            ## delete in left branch
            if self.left:
                self.left  = self.left.delete(val) ## update the left subtree with pruned subtree

        elif val > self.data:
            if self.right:
               self.right = self.right.delete(val) ## update the right subtree with pruned subtree
            # delete eleteme in right branch recurvise
        else: # value equals current node
            
            if self.left is None and self.right is None: # condition 1, the node has no child
                return None
            elif self.left is None:  # condition 2a, the right is there but no left child
                return self.right
            elif self.right is None: # condition 2b, the left is there but no right child
                return self.left
            else: ## condition 3, a node has both a left and a right child
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)  ## update the right subtree with pruned subtree
        
        return self # return the new pruned tree

## Define a function that creates a tree from a list
def build_tree(elements):
    print ('Building a tree')
    root = BinarySearchNode (elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers_tree = build_tree([11,6,8,19,4,10,5,17,43,49,31])
    #print('In order traversal:', numbers_tree.in_order_traversal())
    #print('Searching value', 43, numbers_tree.search(43) )
    print('Deleting value', 17 )
    numbers_tree.delete(17)
    print('In order traversal:', numbers_tree.in_order_traversal())
    numbers_tree.search(14)
    print(numbers_tree.data)
