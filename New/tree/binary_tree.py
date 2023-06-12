

from abc import ABC,abstractclassmethod
# interface class
class binary_tree_interface(ABC):
    '''
    This is the interface class for binary_search
    '''
    @abstractclassmethod
    def binary_tree(val):
        pass
    @abstractclassmethod
    def set_root_val(val):
        pass
    @abstractclassmethod
    def get_root_val(val):
        pass
    @abstractclassmethod
    def get_left_child(self):
        pass
    @abstractclassmethod
    def get_right_child(self):
        pass
    @abstractclassmethod
    def insert_left_child(self):
        pass
    @abstractclassmethod
    def insert_right_child(self):
        pass
# concrete class
class Binary_tree(binary_tree_interface):
    def __init__(self,root_val):
        self.tree=Binary_tree.binary_tree(root_val)
    def binary_tree(val):    
        return [val,[],[]]
    def set_root_val(root,val):
        root[0]=val
    def get_root_val(tree):
        return tree[0]
    def get_left_child(root):
        return root[1]
    def get_right_child(root):
        return root[2]

    def insert_left_child(root,val):
        t=root.pop(1)
        if len(t)>1:
            # if root has left child
            root.insert(1,[val,t,[]])
        else:
            root.insert(1,[val,[],[]])

    def insert_right_child(root,val):
        t=root.pop(2)
        if len(t)>1:
            # if root has right child
            root.insert(2,[val,[],t])
        else:
            root.insert(2,[val,[],[]])



# t=Binary_tree(5)#->creates a binary tree object
# Binary_tree.insert_left_child(t.tree,7)#->inserts a left child to the given root node
# Binary_tree.insert_right_child(t.tree, 6)#->insert a right child to the given root node
# Binary_tree.set_root_val(t.tree, 0)#->changes the root value
# root_t=Binary_tree.get_root_val(t.tree)#->returns the root value of the tree
# left_t=Binary_tree.get_left_child(t.tree)#->return the left subtree of given root
# right_t=Binary_tree.get_right_child(t.tree)#->return the right subtree of given root

# print(t.tree)
# print(root_t)
# print(left_t)
# print(right_t)



t=Binary_tree('a')
Binary_tree.insert_left_child(t.tree,'b')
Binary_tree.insert_right_child(t.tree,'c')
Binary_tree.insert_right_child(Binary_tree.get_left_child(t.tree),'d')

Binary_tree.insert_right_child(Binary_tree.get_right_child(t.tree),'f')
Binary_tree.insert_left_child(Binary_tree.get_right_child(t.tree),'e')
print(t.tree)









