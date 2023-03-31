
class Bomm1:
    def multply(self,a,d):
        return a*d

class Bomm2:
    def devide(self,a,d):
        return a/d

class Bomm3:
    def add(self,a,d):
     return a+d

class Bomm(Bomm1,Bomm2,Bomm3,):
  def subtract(self,a,d):
      return a-d

b = Bomm()
print(b.devide(1800,9))
