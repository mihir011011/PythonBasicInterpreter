'''
Created on Jul 7, 2011

@author: Admin
'''
import abc

class Statement(object):
    '''
    classdocs
    '''
    @abc.abstractmethod
    def execute (self):
        return   

    def __init__(self,statementLine):
        '''
        Constructor
        '''