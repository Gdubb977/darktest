import unittest
import datetime
import sys
from variables_test.python_variables import main as  test_vars
from lists_test.test_list import main as test_list
from dict_test.test_dict import main as test_dict 

class TestClasses(unittest.TestCase):
    def __init__(self):
        self.initiated = True
        self.quiz = None
        self.list_count = 0
        
        
    @classmethod
    def tVariables(self):
        self.quiz = test_vars()
        answers = [str, int, float, list, dict, tuple]
        failed = []
        self.list_count = len(self.quiz[3])
        for key, answer in enumerate(self.quiz):
           
            if type(answer) == answers[key]:
                print("True")
            else: 
                failed.append(answer)
                print(failed)
                raise Exception('Variable type does was incorrect')
            
            
        #self.assertEqual(self,self.quiz, answer)
        
        return
    
    @classmethod
    def tList(self):
        self.quiz = test_list()
        copy_list = self.quiz[0]
        user_list = self.quiz[1]
        
        """if copy_list == user_list:
            raise('The List was not changed')"""
    
        if user_list[-2].lower() != 'dragon fruit':
            raise('Dragon Fruit Not added')

        print('Passed')
    
    @classmethod
    def tDict(self):
        self.quiz = test_dict()
        try:
            if self.quiz.date != datetime.datetime.now():
                raise Exception(f"Times may be off, but the date was added {self.quiz.date}")
        except AttributeError:
            raise Exception('The dictionary does not have a date added')
     
        if not self.quiz.name:
            raise Exception('No named was added for the user.')
       
        
        
     
if __name__ == '__main__':
    options = ['variables', 'list', 'dict', 'classes']
    all_tests = TestClasses()
    while True:
        test_which = input('Which test do you want to run? \n'
                           +'Options: \n \t'
                           + f"{[option for option in options]}: \n Enter Option:  ")
        if test_which.lower() in options:
            match test_which.lower():
                case 'variables':
                    all_tests.tVariables()
                    break
            
                case 'list':
                    all_tests.tList()
                    break
                
                case 'dict':
                    all_tests.tDict()
                    break
            