# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:36:30 2018

@author: zhenl

1. Extend the buildParseTree function to handle mathematical expressions that do not have spaces between every character.
2. Modify the buildParseTree and evaluate functions to handle boolean statements (and, or, and not).
    Remember that “not” is a unary operator, so this will complicate your code somewhat.
3. Using the findSuccessor method, write a non-recursive inorder traversal for a binary search tree.
4. Modify the code for a binary search tree to make it threaded.
    Write a non-recursive inorder traversal method for the threaded binary search tree. 
    A threaded binary tree maintains a reference from each node to its successor.
5. Modify our implementation of the binary search tree so that it handles duplicate keys properly. 
    That is, if a key is already in the tree then the new payload should replace the old rather than add another node with the same key.
"""

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import re

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def buildParseTree(fpexp):
    
    '''requires fully parenthesized expression '''
    
    number_or_symbol = re.compile('(\d+|[^ 0-9])')
    fplist = re.findall(number_or_symbol, fpexp)
#    print( fplist )
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def buildParseTree_bool( fpexp ):
        
    '''requires fully parenthesized expression '''
    
    fpexp = fpexp.strip()
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['and', 'or']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            
        elif i == 'not':
            parent = pStack.pop()
            currentTree = parent
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            
        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['and', 'not', 'or', ')', '(']:
            try:
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid Boolean".format(i))
                
    return eTree
if __name__ == "__main__":
#    buildParseTree("( (10+k ) * 3 )").postorder()
    buildParseTree( "(( (10+5 ) * 3 )/32)" ).postorder()
    buildParseTree_bool( "( True and False )" ).postorder()
    buildParseTree_bool( "( not ( True and False ) )" ).postorder()
    buildParseTree_bool( "( not ( ( True and False ) or True ) )" ).postorder()