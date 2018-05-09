 def getHeight(self,node):
        #Write your code here
  
        if node is None:
            return -1 ; 

        else :

            # Compute the depth of each subtree
            lDepth = self.getHeight(node.left)
            rDepth = self.getHeight(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
 