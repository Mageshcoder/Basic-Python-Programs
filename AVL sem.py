import sys
class treenode(object):
   def __init__(self,key):
      self.key=key
      self.left=None
      self.right=None
      self.height=1

class AVLtree(object):
   def insert(self,root,key):
      if not root:
         return treenode(key)
      elif key<root.key:
         root.left=self.insert(root.left,key)
      else:
         root.right=self.insert(root.right,key)
      root.height=1+max(self.getheight(root.left),self.getheight(root.right))

      balancefactor=self.getbalance(root)
      if balancefactor>1:
         if key<root.left.key:
            return self.rightRotate(root)
         else:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)

      if balancefactor<-1:
         if key>root.right.key:
            return self.leftRotate(root)
         else:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
      return root

   def getheight(self,root):
      if not root:
         return 0
      return root.height

   def getbalance(self,root):
      if not root:
         return 0
      return self.getheight(root.left)-self.getheight(root.right)

   def getminvaluenode(self,root):
      if root is None or root.left is None:
         return root
      return self.getminvaluenode(root.left)

   def preorder(self,root):
      if not root:
         return
      print("{0}",format(root.key),end=" ")
      self.preorder(root.left)
      self.preorder(root.right)

   def printhelper(self,currptr,indent,last):
      if currptr != None:
         sys.stdout.write(indent)
         if last:
            sys.stdout.write("R----")
            indent +="    "
         else:
            sys.stdout.write("L----")
            indent +="    "
         print(currptr.key)
         self.printhelper(currptr.left, indent,False)
         self.printhelper(currptr.right,indent,True)


myTree=AVLtree()
root=None
nums=[33,13,52,9,21,61,8,11]
for num in nums:
   root=myTree.insert(root,num)
myTree.printhelper(root," ",True)


print("""R----33
     L----13
         L----9
             L----8
             R----11
         R----21
     R----52
         R----61""")
