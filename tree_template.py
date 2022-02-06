#!/usr/bin/env python3

def Basic():

    class Tree:
        def __init__(self):
            self.val = None
            self.left = None
            self.right = None

    def visit(node):
       print(node.val)

    def recv_preorder(node):
        visit(node)
        preorder(node.left)
        preorder(node.left)

    def recv_inorder(node):
        inorder(node.left)
        visit(node)
        inorder(node.left)

    def recv_postorder(node):
        postorder(node.left)
        postorder(node.left)
        visit(node)
    


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
