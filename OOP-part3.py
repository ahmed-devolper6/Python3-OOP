class Studand:
    def __init__(self,name):
        print(f"the sudand name is {name}")
        print("the marks is: ")
        self.marks = []
    def print_marks(self):
        print(self.marks)
    def add_mark(self,mark):
        medtreams = 5
        self.marks.append(mark + medtreams)
ahmed = Studand("ahmed")
ahmed.add_mark(20)
ahmed.add_mark(40)
ahmed.add_mark(30)
ahmed.add_mark(80)
ahmed.add_mark(50)
ahmed.print_marks()
