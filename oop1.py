class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0

        for val in self.marks:
            sum += val

        x = sum / len(self.marks)

        print(self.name + "'s average marks are: " + str(x))

s1 = student("John", [90, 85, 95])
s2 = student("Alice", [85, 80, 90])
s1.get_avg()
s2.get_avg()