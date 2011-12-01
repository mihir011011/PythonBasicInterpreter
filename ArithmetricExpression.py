'''
Created on Jul 8, 2011

@author: Admin
'''
import config
import sys

class ArithmetricExpression(object):
    '''
    classdocs
    '''

    express = 'cat'
    def __init__(self, statement):
        '''
        Constructor
        '''
        self.statement = statement
        
    def getExpression(self):
        # Sets arithExpress to anything after the equal sign
        arithExpress = self.statement[self.statement.find('=') + 1::].rstrip()
        # If the Key isn't found in the dictionary throw an error
        try:
                # If part of the arithmetic expression is a variable replace it with the variable value
            arithExpress = ArithmetricExpression.replaceVar(self, arithExpress)
            # returns the result of the arithmetic expression
            return  int(eval(arithExpress))
        except KeyError:
            sys.stderr.write('Undeclared Variable in line : ' + self.statement)
            sys.exit()
            
            
    def replaceVar(self, statement):
        i = 0
        while i < len(statement):
            if statement[i] in config.variables:
                strVariable = str(config.variables[statement[i]])
                statement = statement.replace(statement[i], strVariable)
            i += 1
        return statement
