#!/usr/bin/env python3

def Basic():

    class Tree:
        def __init__(self):
            self.val = None
            self.left = None
            self.right = None

    def recursive():
        def visit(node):
           print(node.val)
        def preorder(node):
            visit(node)
            preorder(node.left)
            preorder(node.left)
        def inorder(node):
            inorder(node.left)
            visit(node)
            inorder(node.left)
        def postorder(node):
            postorder(node.left)
            postorder(node.left)
            visit(node)

def Advanced():
    def iterative():
        def visit(node):
           print(node.val)
        def preorder(root):
            stack = [root]
            while len(stack) > 0:
                node = stack.pop()
                if node is not None:
                    visit(node)
                    stack.append(node.left)
                    stack.append(node.right)
        def inorder(root):
            cur, stack = root, []
            while cur is not None or len(stack) > 0:
                if cur is not None:
                    stack.append(cur)
                    cur = cur.left
                else:
                    node = stack.pop()
                    visit(node)
                    cur = node.right
        def postorder(root):
            pass
    
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1
    def diameter(node):
        if node is None:
            return 0
        return max(
            height(node.left) + height(node.right),
            max(diameter(node.left), diameter(node.right))
        )
    
    def lowest_common_ancestor():
        pass


def Trie():

    class TrieNode:
        def __init__(self):
            self.is_word = False
            self.next = {}
    class Trie:
        def __init__(self):
            self.root = TrieNode()
        def add(self, word):
            cur = self.root
            for c in word:
                if c not in cur.next:
                    cur.next[c] = TrieNode()
                cur = cur.next[c]
            cur.is_word = True
        def search(self, word):
            cur = self.root
            for c in word:
                if c not in cur.next:
                    return False
                cur = cur.next[c]
            return cur.is_word
        def startswith(self, word):
            cur = self.root
            for c in word:
                if c not in cur.next:
                    return False
                cur = cur.next[c]
            return True
