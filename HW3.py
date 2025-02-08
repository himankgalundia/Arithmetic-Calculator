# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__


#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if len(self)==0:   # checking if len of stack is zero  using len method 
            return True
        else:
            return False


    def __len__(self): 
        # YOUR CODE STARTS HERE
        count=0
        current=self.top
        while current is not None:   # using while loop and traversing through the stack and counting the number of times the loop runs 
            count+=1
            current=current.next
        return count

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode=Node(value)  # makes a new node object
        newNode.next=self.top # and pushes to the top of the stack 
        self.top=newNode
        

    def pop(self): 
        # YOUR CODE STARTS HERE
        if len(self)==0:  
            return None
        else:
            pop_value=self.top.value  # removes the top item from stack and returns its value
            self.top=self.top.next
            return pop_value


    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value # returns the top value of the stack 



#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        txt=txt.strip()   # checking if the str can be converted to a float 
        try:
            float(txt)
        except:       # if not then raising an error 
            return False
        return True



    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('( ( ( ( ( ( 5.6 + 4 ) - ( 5 ^ 2 ) ) /  ( 5 - -2 ) ) ) + 7 ) * 3 )')
            '5.6 4.0 + 5.0 2.0 ^ - 5.0 -2.0 - / 7.0 + 3.0 *'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        if len(txt)==0:
            return False
        if self._getPostfix_helper(txt)== False: # using helper fuction to check if expression is valid or not 
            return None
        txt=txt.strip().split()
        precendence_d={'^':1, '/':2, '*': 2, '+':3, '-':3, '(':4, '{':5,'[':6, ')':4,'}':5,']':6} # making a dictionary for precedence order
        in_open={'(':4, '{':5,'[':6}
        in_close={')':4,'}':5,']':6}
        txt=self._getPostfix_helper_parenthesis_multiply(txt)  # using an helper function for implicite multiplication 
        i=0
        lenght=len(txt)
        postfix=''
        while i<lenght: # using the while loop for converting infix to postfix expression till the end of expression 
            if self._isNumber(txt[i]):  # if txt[i] is a number add to the str with a space
                postfix+= str(float(txt[i])) +' '
            
            if not self._isNumber(txt[i]):  # if not number then 
                if postfixStack.isEmpty():   # if stack is empty push operator or paranthesises in stack
                    postfixStack.push(txt[i])
                else:
                    if txt[i] in in_open:   # if it is an open paranthesises push to stack 
                        postfixStack.push(txt[i])
                    
                    elif txt[i] in in_close: # if it is an cloased paranthesises then 
                        while postfixStack.peek() not in in_open:  # now poping all items till an open parenthesises comes and poping open parenthesises also
                                postfix+= postfixStack.pop()+' '
                        postfixStack.pop() #  open parenthesises also popped 
                    else:
                            if txt[i]=='^' and postfixStack.peek()=='^': # if top of stack is '^' and txt[i] is also '^' then pusch txt[i] in the stack
                                postfixStack.push(txt[i]) 
                            else:
                                while not postfixStack.isEmpty() and precendence_d[postfixStack.peek()] <= precendence_d[txt[i]]:
                                        postfix += postfixStack.pop()+' ' # #Lower the value in dict, higher is the priority. We must ignore open parentheses as they are being dealt with differently
                                postfixStack.push(txt[i])
            i+=1
        while not postfixStack.isEmpty(): # if stack is not empty then adding all the remaining items to str 
            postfix+=postfixStack.pop()+' '
        return postfix.strip()

    def _getPostfix_helper_parenthesis_multiply(self,txt):
        in_open={'(':4, '{':5,'[':6}
        in_close={')':4,'}':5,']':6}
        for i in range(len(txt)-1):   # using for loop to do implicit multipication 
            if self._isNumber(txt[i]) and txt[i + 1] in in_open:  # if i is a number and i+1 is an open parenthesises then insert '*'
                txt.insert(i + 1, '*') 
            elif self._isNumber(txt[i+1]) and txt[i] in in_close: # if i+1 is a number and i-1 is an closed paranthesises then insert '*' 
                txt.insert(i, '*')
            elif  txt[i] in in_close and txt[i+1] in in_open:  # if i is a closed parenthesises and i+1 is open parenthesises then insert '*'
                txt.insert(i+1, '*')
        return txt

    def _getPostfix_helper_balanced_parenthesis(self,txt):
        fixStack = Stack()
        txt=txt.strip().split(' ')
        in_open={'(':4, '{':5,'[':6}
        in_close={')':4,'}':5,']':6}
        for i in range(len(txt)):  # using for loop 
            if txt[i] in in_open:  # if txt[i] an open parenthesises then push it in stack
                fixStack.push(txt[i])  
            elif txt[i] in in_close:  # if txt[i] a closed parenthesises and stack is empty return False
                if fixStack.isEmpty(): 
                    return False
                else:
                    if in_close[txt[i]]!=in_open[fixStack.pop()]:  # if stack is not empty then if there values in dictionary are not equal then return false
                        return False
        if not fixStack.isEmpty(): # and if stack is not empty return False
            return False


    def _getPostfix_helper(self, txt):
        in_open={'(':4, '{':5,'[':6}
        in_close={')':4,'}':5,']':6} 
        operators = ['^', '*', '/', '+', '-']
        if self._getPostfix_helper_balanced_parenthesis(txt)==False:
            return False
        txt=txt.strip().split(' ')
        #Now checking for Unsupported operators 
        if txt[0] not in in_open and txt[0] not in in_close: # if first item not an open paranthesises and not an closed parenthesises 
            if txt[0] in operators: #Testing for expressions: / 4 * 5 + 6 
                return False

        if txt[-1] not in in_open  and txt[-1] not in in_close: 
            if txt[-1] in operators: #Testing for expression:  4 * 5 + 6 +
                return False

        for i in range(len(txt)):
            if txt[i] not in in_open and txt[i] not in in_close: # if it is not an open paranthesises and not an closed parenthesises
                if not self._isNumber(txt[i]) and txt[i] not in operators:#Testing expression: 4 @ 5 + 6 - 7 and checking for proper floats
                    return False

        for i in range(len(txt)-1):
            if self._isNumber(txt[i]) and self._isNumber(txt[i+1]): # if txt[i] is a number and i+1 is a number 
                return False #Testing for expressions : 4 * 5 + 6 7
            if txt[i] in operators and txt[i+1] in operators: #Testing for expressions : 4 * 5 + - 6 
                return False



    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures


            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            >>> x.setExpr('4.5 ( 89.5 + 9 ) + ( 89 - -8 ) 3' )
            >>> x.calculate
            734.25
            >>> x.setExpr('[ ( { ( ( [ ( ( 45.63574 ) ) ] ) ) } ) ]')
            >>> x.calculate
            45.63574


            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the expression

        # YOUR CODE STARTS HERE
        new_expr=self._getPostfix(self.getExpr)  # converting expresion to postfix 
        if new_expr==None:
            return None
        new_expr=new_expr.split(' ')
        i=0
        for i in range(len(new_expr)):  # using for loop and if ch is number then push it in stack 
            if self._isNumber(new_expr[i]):
                calcStack.push(new_expr[i])
            elif not self._isNumber(new_expr[i]):  # if not a number then pop first two numbers from stack and oprate then with the operator value of new expr
                num1=float(calcStack.pop())
                num2=float(calcStack.pop())
                if new_expr[i]=='+':
                    calcStack.push(num2 + num1)  # adding numbers if ch is '+' and pushing it to stack 

                elif new_expr[i]=='-':
                    calcStack.push(num2 - num1) # substrating  numbers if ch is '-' and pushing it to stack 

                elif new_expr[i]=='*':
                    calcStack.push(num2 * num1) # multiplying numbers if ch is '*' and pushing it to stack 

                elif new_expr[i]=='/' and num1!=0.0 :
                    calcStack.push(num2 / num1)  # division numbers if ch is '/' and pushing it to stack 

                elif new_expr[i]=='^':
                    calcStack.push(num2 ** num1) 
            i+=1
        return float(calcStack.pop()) # poping the final item in stack 



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        word=word.strip()
        if not word[0].isalpha():  # if first ch in word is not an alphabet return false
            return False
        for i in range(len(word)):
            if not word[i].isalnum(): # if ch is not an number and alphabet then return false
                return False
        else:
            return True # else return false 
    

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        expr=expr.strip()
        expr=expr.split(' ')
        new_expr=''
        for i in range(len(expr)):  # using for loop to replace variables 
            if expr[i] in self.states:  # if in self. states 
                new_expr+=str(self.states[expr[i]])+ ' '  # replace variable
            elif self._isVariable(expr[i]): # if not variable 
                return None
            else:
                new_expr+=expr[i]+' ' # else a number is added to string 
        return new_expr.strip()

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        new_d={}
        expressions=self.expressions.split(';')
        lines_list=expressions.copy()
        for i in range(len(lines_list)):
            expr=lines_list[i].split('=') # # Splitting each line into variable and expression
            
            if self._isVariable(expr[0]): # Checking if the left-hand side is a variable
                expr[1]=self._replaceVariables(expr[1]) # # Replacing variables in the expression
                calcObj.setExpr(expr[1]) # # Setting the expression for calculation using calcObj
                self.states[expr[0].strip()]=float(calcObj.calculate)
                new_str = self.states.copy() # Creating a copy of the current state
                new_d[lines_list[i]]=new_str

            elif len(lines_list)-1==i:
                lines_list[i]=lines_list[i].split(' ')
                del lines_list[i][0]
                exp=' '.join(lines_list[i])
                exp=self._replaceVariables(exp)  # Replacing variables in the last expression
                calcObj.setExpr(exp)
                new_d['_return_']=float(calcObj.calculate)

            else: # unexpected cases by returning None
                self.states={}
                return None
        return new_d



def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples( Calculator._getPostfix , globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()