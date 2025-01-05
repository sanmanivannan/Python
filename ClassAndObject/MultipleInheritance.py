class Father():
    def dad_skills(self):
        print("dad skills")

class Mother():
    def mom_skills(self):
        print("mom skills")

class Child(Father,Mother):
    def child_skills(self):
        print("child skills")
        print("+++++++++++++++++++++++++++++++++")

c = Child()
c.mom_skills()
c.dad_skills()
c.child_skills()

#=====================================================================

class Father():
    def skills(self):
        print("dad skills")

class Mother():
    def skills(self):
        print("mom skills")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("child skills")

c = Child()
c.skills()