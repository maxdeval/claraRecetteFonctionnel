def setUp(self):
    App.open("Google Chrome")

def tearDown(self):
    App.close("Google Chrome")

def testClara():
    click("1526994917663.png")
    paste("https://mae-attempt.herokuapp.com/")
    type(Key.ENTER)
    assert exists(Pattern("1526995285010.png").targetOffset(-26,100))
    
testClara()