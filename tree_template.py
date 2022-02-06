#!/usr/bin/env python3

class Tree:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


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


