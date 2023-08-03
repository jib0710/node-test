class JSS:
   
    def __init__(self, name:str, age:int, position:str):
        self.name = name
        self.age = age
        self.position =position
    def show(self):
        print("제 이름은 {}, 나이는 {}세 이고 직급은 {}입니다.".format(self.name, self.age, self.position))
    def upAge(self):
        self.age += 1
        
    def reposition(self):
        self.position = input("새로운 직급: ")
a = JSS("장이범", 17, "대학생")
a.show()
a.upAge()
a.show()
a.reposition()
a.show()



