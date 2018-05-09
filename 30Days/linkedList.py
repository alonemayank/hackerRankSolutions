  def insert(self,head,data): 
    #Complete this method
        
        node = Node(data)
        if head is None:
            head = node
            return head
        
        temp = head
        
        while temp.next is not None:
            temp = temp.next
        
        temp.next = node
        return head
  
  