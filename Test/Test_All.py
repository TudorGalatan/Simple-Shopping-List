from Test.Test_Domain import TestDomain
from Test.Test_Repository import TestRepository



def runTests ():
    
    '''
        Description: runs all the tests
        Input: none
        Output: true, if all the tests pass (all the functionalities work correctly)
                false, otherwise
    '''
    
    test_domain = TestDomain()
    test_repository = TestRepository()
    
    test_domain.runDomainTests()
    test_repository.runRepositoryTests()