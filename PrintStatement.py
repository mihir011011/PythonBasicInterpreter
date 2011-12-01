'''
Created on Jul 7, 2011

@author: Admin
'''
from Statement import Statement
import config
import sys
class PrintStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, statementLine):
        super (PrintStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):
        
        printStatement = self.statement.split()
        if(config.variables[printStatement[2]] == 'null'):
            sys.stderr.write('Undeclared Variable in line : '+ self.statement)
            sys.exit()
        else:
            print(config.variables[printStatement[2]])