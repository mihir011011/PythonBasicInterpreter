'''
Created on Jul 8, 2011

@author: Admin
'''
import config
import sys
class Variable(object):
    '''
    classdocs
    '''

    
    def __init__(self,statement):
        '''
        Constructor
        '''
        self.statement = statement
        
    def getVariable(self):
        return
    
    def setVariable(self,expression):
        varStatement = self.statement.split()
        if(varStatement[2] in config.variables):
            config.variables[varStatement[2]] = expression    
        else:
            sys.stderr.write('Invalid Variable in line : '+ self.statement)
            sys.exit()
