from abc import abstractmethod
from .bin_search_tree import BSTree


class BinTreeTraverse:
  def __init__(self, root):
    self.root = root
    self._visited_order = []
  
  @abstractmethod
  def traverse(self, root):
    raise NotImplemented('Must implement in derived classes.')
  
  def _visit(self, node):
    self._visited_order.append(node.val)

  def _done(self):
    print(self._visited_order)
    
    
 class InorderBinTreeTraverse(BinTreeTraverse):
  def __init__(self, root):
    super().__init__(root)

  def traverse(self, root):
    self._inorder(root)
    self._done()

  def _inorder(self, node):
    if node is None:
      return
    self._inorder(node.left)
    self._visit(node)
    self._inorder(node.right)
    
    
class PreorderBinTreeTraverse(BinTreeTraverse):
  def __init__(self, root):
    super().__init__(root)

  def traverse(self, root):
    self._preorder(root)
    self._done()

  def _preorder(self, node):
    if node is None:
      return
    self._visit(node)
    self._preorder(node.left)
    self._preorder(node.right)
    
    
class PostorderBinTreeTraverse(BinTreeTraverse):
  def __init__(self, root):
    super().__init__(root)
  
  def traverse(self, root):
    self._postorder(root)
    self._done()

  def _postorder(self, node):
    if node is None:
      return
    self._postorder(node.left)
    self._postorder(node.right)
    self._visit(node)
