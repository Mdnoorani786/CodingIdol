#single inheritance 
class osama:
  def show(osama):
    print("He is honest")
class brother(osama):
  def Name(self):
    print("his brother's name is Saif")
    
obj=brother()
obj.show()
obj.Name()
 #multiple inheritance
class father:
  def myfun(father):
    print("what")
class son():
  def myname(self):
    print("son name?" )
class daughter(father,son):
    pass
    
obj=daughter()
obj.myfun()
obj.myname()
#multiple level inheritance
class Alam:
  def fun(Alam):
    print("Alam")
class Md(Alam):
  def sun(self):
    print("Md")
class Noorani(Md):
  def nun(self):
    print("Noorani")
    
abj=Noorani()
abj.sun()
abj.fun()
abj.nun()
    
    
    
    
    
    
    
    
    
    