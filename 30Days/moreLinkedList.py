   def removeDuplicates(self,head):
        #Write your code here
        temp = head
        while head.next!=None:
            temp1 = head.next
            if head.data == temp1.data:
                while temp1!=None and temp1.data==head.data:
                    temp1=temp1.next
                head.next=temp1
            if head.next != None:
                head=head.next
            
        return temp
  