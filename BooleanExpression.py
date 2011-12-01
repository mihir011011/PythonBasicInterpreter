'''
Created on Jul 11, 2011

@author: Admin
'''
import config
class BooleanExpression(object):
    '''
    classdocs
    '''


    def __init__(self,booleanStatement):
        '''
        Constructor
        '''
        self.booleanStatement = booleanStatement
        
    def compare(self):
        expression = self.booleanStatement[self.booleanStatement.find('IF') + 3:self.booleanStatement.find('GOTO')].rstrip()
        expression = BooleanExpression.replaceVar(self,expression)
        splitExpression = expression.split()
        result = False
        if '<=' in expression:
            if int(splitExpression[0]) <= int(splitExpression[2]):
                result = True
        elif '=' in expression:
            if int(splitExpression[0]) == int(splitExpression[2]):
                result = True
        elif '>=' in expression:
            if int(splitExpression[0]) >= int(splitExpression[2]):
                result = True
        elif '<>' in expression:
            if int(splitExpression[0]) != int(splitExpression[2]):
                result = True
        elif '<' in expression:
            if int(splitExpression[0]) < int(splitExpression[2]):
                result = True
        elif '>' in expression:
            if int(splitExpression[0]) > int(splitExpression[2]):
                result = True
        else:
            result = False
        return result
    
    def replaceVar(self,statement):
        i = 0
        while i < len(statement):
            if statement[i] in config.variables:
                strVariable = str(config.variables[statement[i]])
                statement = statement.replace(statement[i],strVariable)
            i += 1
        return statement