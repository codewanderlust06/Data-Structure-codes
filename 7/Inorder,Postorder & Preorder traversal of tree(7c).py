class Node:  
    def __init__(self,data):   
        self.data = data  
        self.left = None  
        self.right = None  

class BinaryTree:  
    def __init__(self):  
        self.root = None
    def insertNode(self, data):    
        newNode = Node(data)           
        #Check whether tree is empty  
        if(self.root == None):  
            self.root = newNode  
            return  
        else:  
            queue = []  
            #Add root to the queue  
            queue.append(self.root)                
            while(True):  
                node = queue.pop(0)  
                #If node has both left and right child, add both the child to queue  
                if(node.left != None and node.right != None):  
                    queue.append(node.left) 
                    queue.append(node.right) 
                else:  
                    #If node has no left child, make newNode as left child  
                    if(node.left == None):  
                        node.left = newNode  
                        queue.append(node.left)
                    else:  
                        #If node has left child but no right child, make newNode as right child  
                        node.right = newNode;  
                        queue.append(node.right)  
                    break;  
                       
    def inorderTraversal(self, node):            
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty")  
            return;  
        else:  
            if(node.left != None):  
                self.inorderTraversal(node.left)  
            print(node.data),  
            if(node.right!= None):  
                self.inorderTraversal(node.right)

    def preorderTraversal(self, node):            
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty") 
            return 
        else:
            print(node.data)
            if(node.left != None):  
                self.preorderTraversal(node.left)    
            if(node.right!= None):  
                self.preorderTraversal(node.right)

    def postorderTraversal(self, node):            
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty")  
            return;  
        else:           
            if(node.left != None):  
                self.postorderTraversal(node.left)   
            if(node.right!= None):  
                self.postorderTraversal(node.right)
            print(node.data)
                  
bt = BinaryTree();  
#Add nodes to the binary tree     
bt.insertNode(1);    
bt.insertNode(2);  
bt.insertNode(3);
bt.insertNode(4);  
bt.insertNode(5);
bt.insertNode(6);  
bt.insertNode(7);

print("Binary tree in inorder traversal after insertion");   
bt.inorderTraversal(bt.root);

print("Binary tree in preorder traversal after insertion");   
bt.preorderTraversal(bt.root);

print("Binary tree in postorder traversal after insertion");   
bt.postorderTraversal(bt.root);  
   
