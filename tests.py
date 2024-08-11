import unittest
import sys
from variables_test.python_variables import main as  test_vars
class TestClasses(unittest.TestCase):
    def __init__(self):
        self.initiated = True
        self.quiz = None
        
        
    @classmethod
    def tVariables(self):
        self.quiz = test_vars()
        answers = [str, int, float, list, dict, tuple]
        failed = []
        for key, answer in enumerate(self.quiz):
           
            if type(answer) == answers[key]:
                print("True")
            else: 
                failed.append(answer)
                print(failed)
                raise Exception('Variable type does was incorrect')
                sys.exit(0)
            
        #self.assertEqual(self,self.quiz, answer)
        
        return
    

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
                    
            