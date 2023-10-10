class user:
    name = None
    email = None

    def __init__(self, name, email):
        self.name = name
        self.email = email


    def send_email(self):
        if self.email is not None:
            print("sending email: "+ self.email)

        else:
            print("erroor")

    def send_name(self):
        if self.name is not None:
            print("username: "+ self.name)

        else:
            print("erroor")








class Student (user):
   
    def is__approved (self):
        return self.score>=8
   
    def __str__(self):
           return "Student: "+str(self.id)+", "+self.email
       
    def __repr__(self):
        return f"Student(name='{self.name}',email='{self.email}',id='{self.id}', score='{self.score}')"
   
   
   
   
   
    id =None
    score = None

    def __init__(self,
    name = None,
    email = None,
    id=None ,
    score=None
    ):
       

       super().__init__(name, email)
       self.id = id
