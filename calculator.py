# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pythonds.basic.stack import Stack

def calculator_expr_check( toklist ):
    opTokens = "*/+-"
    parenTokens = "()"
    notbeginTokens = "*/+-)"
    notendTokens = "*/+-("
    if len( toklist ) == 0: 
        print( "expression check: error. No expr")
        return False
    if toklist[0] in notbeginTokens:
        print( "expression check: error.", "Expression begins with ",toklist[0])
        return False;
    if toklist[-1] in notendTokens:
        print( "expression check: error.", "Expression ends with ",toklist[-1])
        return False;
    for i in range( len(toklist) - 1 ):
        token = toklist[i]
        token_n = toklist[i+1]
        if token.isdigit():
            if token_n == "(" or token_n.isdigit():
                print( "expression check: error", token, token_n )
                return False;
            else:
                continue
        elif token in opTokens:
            if token_n == ")":
                print( "expression check: error", token, token_n )
                return False;
            else:
                continue
        elif token == "(":
            if token_n in parenTokens or token_n in opTokens:
                print( "expression check: error", token, token_n )
                return False;
            else:
                continue
        elif token == ")":
            if token_n.isdigit() or token_n in parenTokens :
                print( "expression check: error", token, token_n )
                return False;
            else:
                continue
    return True

def process( numStack, opStack ):
        op2 = numStack.pop()
        op1 = numStack.pop()
        op = opStack.pop()
        return numStack.push( doMath( op, op1, op2 ) )
    
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
            print("error: divide by zero")
            return None
        else:
            return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def calculatorEval( toklist ):
    opTokens = "*/+-"
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    numStack = Stack()
    opStack = Stack()
    for tok in toklist:
        if tok.isdigit():
            numStack.push( int(tok) )
        elif tok in opTokens:
            if opStack.isEmpty():
                opStack.push( tok )
            else:
                if prec[ tok ] > prec[ opStack.peek() ] :
                    opStack.push( tok )
                else:
                    process( numStack, opStack )
                    opStack.push( tok )
        elif tok == "(":
            opStack.push( tok )
        elif tok == ")":            
            while opStack.peek() != "(":
                process( numStack, opStack )
            opStack.pop()
        
    while not opStack.isEmpty():        
        process( numStack, opStack )
            
    return numStack.pop()

def calculator_paren_check( toklist ):
    parenList = []
    for p in toklist:
        if p == '(' or p == ')':
            parenList.append( p )
    parenExpr = ''.join(parenList)
    if not parChecker(parenExpr):
        print( "error: parentheses not balanced")
        return False
    else:
        return True;
    
def calculator():
    toklist = []
    legalopTokens = "*/+-()"
    while True:
        print ("Enter a number or operator for calculator: ")
        expr = input().strip()
        if expr in legalopTokens or expr.isdigit():
            toklist.append( expr )
        elif expr == "=":
            break;
        else:
            print("input error: invalid token")
            
    if calculator_expr_check( toklist ) and calculator_paren_check( toklist ):        
        print( calculatorEval( toklist ) )
    else:
        return("Error: invalid expression")
    return;
    
if __name__ == "__main__":
    calculator();