    def printinrange(self,root,x,y): #8,5,6,5.5,7,10,9,9.5,11
        if root is None:
            return 
        if root.data>=x and root.data<=y:  #8>=6 8<=10,6=6 6<10,7>6 7<10,10>6 10=10,9>6 9<10,9.5>6 9.6<10
            self.printinrange(root.left,x,y)   #8.left=5,7.left=None, 10.left=9,9.left=None,        
            print(root.data,end=" ")  #6,7,8,9,9.5,10
            self.printinrange(root.right,x,y)  #6.right=7,7.right=None,8.right=10,9.right=9.5,9.5.right=None,10.right=11,
        elif root.data<x: #5<6,5.5<6,
            self.printinrange(root.right,x,y) #5.right=6 ,5.5.right=None
        else:
            self.printinrange(root.left,x,y)