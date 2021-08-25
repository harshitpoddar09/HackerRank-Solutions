# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    def h(root):
        if not root:
            return 0
        lheight=h(root.left)
        rheight=h(root.right)
        return max(lheight,rheight)+1
    return h(root)-1
