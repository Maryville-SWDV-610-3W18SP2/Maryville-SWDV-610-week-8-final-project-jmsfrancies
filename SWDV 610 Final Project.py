from graphics import *
def logic(firstName,lastName):
   print()
   x = input("Enter a capital letter: ")
   y = input("Enter a second capital letter: ")
   z = input("Enter a third capital letter: ")
   a = input("Enter a fourth capital letter: ")
   win = GraphWin("Logic, Logic, Logic!",700,500)
   win.setBackground("Yellow")
   Slogan = Text(Point(350,250),"""Hello, {0} {1}!
Enjoy Learning some Logic.
The (=>) conditional if then, statement.
The '&' the conjunction, and the 'v'
Disjunction symbol.
ENJOY!""".format(firstName,lastName))
   Slogan.setTextColor("black")
   Slogan.setSize(22)
   Slogan.draw(win)
   win.getMouse()
   win.getMouse()
   win.getMouse()
   Slogan.undraw()
   Slogan = Text(Point(350,150),"Ready or Not, Here comes some Logic!")
   Slogan.setTextColor("blue")
   Slogan.setSize(28)
   Slogan.draw(win)
   win.getMouse()
   Slogan.undraw()
   if win.getMouse():
     Title = Text(Point(350,150),"Disjunctive Syllogism")
     Title.setTextColor("blue")
     Title.setSize(20)
     Disjunctive = Text(Point(350,250),("""{0} v {1}
~{0},
{1}""".format(x,y)))
     Disjunctive.setTextColor("black")
     Disjunctive.setSize(22)
     Title.draw(win)
     Disjunctive.draw(win)
   if win.getMouse():
      Title.undraw()  
      Disjunctive.undraw()  
      Title = Text(Point(350,150),"Modus Ponens")
      Title.setTextColor("blue")
      Title.setSize(20)
      ModusPonens = Text(Point(350,250),"""{0} => {1}
{0}
{1}""".format(x,y))
      ModusPonens.setTextColor("black")
      ModusPonens.setSize(22)
      ModusPonens.draw(win)
      Title.draw(win)
   if win.getMouse():
    Title.undraw()
    ModusPonens.undraw()
    Title = Text(Point(350,150),"Modus Tollens")
    Title.setTextColor("blue")
    Title.setSize(20)
    ModusTollens = Text(Point(350,250),"""{0} => {1}
~{1}
~{0}""".format(x,y))
    ModusTollens.setTextColor("black")
    ModusTollens.setSize(22)
    Title.draw(win)
    ModusTollens.draw(win)
    if win.getMouse():
      Title.undraw()
      ModusTollens.undraw()
      Title = Text(Point(350,150),"Conjunction")
      Title.setTextColor("blue")
      Title.setSize(20)
      Conjunction = Text(Point(350,250),"""{0} & {1}
{0}
{1}""".format(x,y))
      Conjunction.setTextColor("black")
      Conjunction.setSize(22)
      Title.draw(win)
      Conjunction.draw(win)  
    if win.getMouse():
      Title.undraw()
      Conjunction.undraw()
      Title = Text(Point(350,150),"Hypothetical Syllogism")
      Title.setTextColor("blue")
      Title.setSize(20)
      Hypothetical = Text(Point(350,250),"""{0} => {1}
{1} => {2}
{0} => {2}""".format(x,y,z))
      Hypothetical.setTextColor("black")
      Hypothetical.setSize(22)
      Title.draw(win)
      Hypothetical.draw(win)  
    if win.getMouse():
      Title.undraw()
      Hypothetical.undraw()
      Title = Text(Point(350,150),"Material Implication")
      Title.setTextColor("blue")
      Title.setSize(20)
      Material = Text(Point(350,250),"""(~{0} v {1})
({0} => {1})""".format(x,y))
      Material.setTextColor("black")
      Material.setSize(22)
      Title.draw(win)
      Material.draw(win)
    if win.getMouse():
      Title.undraw()
      Material.undraw()
      Title = Text(Point(350,150),"Dilemma")
      Title.setTextColor("blue")
      Title.setSize(20)
      Dilemma = Text(Point(350,250),"""{0} v {1}
{0} => {2}
{1} => {3}
{2} v {3}
""".format(x,y,z,a))
      Dilemma.setTextColor("black")
      Dilemma.setSize(22)
      Title.draw(win)
      Dilemma.draw(win)
      win.getMouse()
    if win.getMouse():
      Title.undraw()
      Dilemma.undraw()
      Title = Title = Text(Point(350,150),"Enjoy having a logic filled life! ")
      Title.setTextColor("blue")
      Title.setSize(30)
      Title.draw(win)
      win.getMouse()
      win.close() 
def main():
  permission = input("Would you like to create a username(y/n): ")
  if permission == "n":
      print("Have a Great Day! ") 
  if permission == "y":
      while True:
        firstName = input("Enter Your First Name: ")
        lastName = input("Enter Your Last Name: ")
        username = input("Enter a username with letters: ")
        password = input("Enter a password with a length of more than 8 characters: ")
        if not firstName.isalpha() or not lastName.isalpha() or not username.isalpha() or not len(password) >= 8:
          print("Error: One or More conditions haven't been met: ") 
          continue
        else:
            print("""First Name is: {0}
Last Name is: {1}
UserName is: {2}
password is: {3}""".format(firstName,lastName,username,password))
        break
      while True: 
        enter1 = input("Enter UserName: ")
        enter2 = input("Enter Password: ")
        if enter1 == username and enter2 == password:
           logic(firstName,lastName)
           break
        else:
           print("Enter a valid username and password: ")
           continue
        
        
main()          