def levelOrder(self,root):
        #Write your code here
        node = root
        li = []
        while node:
            # print(len(li))
            print(node.data,end=' ')
            if(node.left!=None):
                li=[node.left]+li
                # root=root.left
            if node.right!=None:
                li=[node.right]+li
                # root=root.right
            node=li.pop()