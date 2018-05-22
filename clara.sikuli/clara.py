def setUpChrome():
    App.open("Google Chrome")

def closeChrome():
    App.close("Google Chrome")

def setUpClara():
    App.open("Google Chrome")
    click("1526994917663.png")
    paste("https://mae-attempt.herokuapp.com/")
    type("Key.ENTER")
    assert exists(Pattern("1526995285010.png").targetOffset(-26,100))
    
    