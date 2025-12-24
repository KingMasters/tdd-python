from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None
        self.wasSetUp = None
        self.name = name

    def testMethod(self):
        self.wasRun = 1
  
    def setUp(self):
        self.wasRun = None
        self.wasSetUp= 1

