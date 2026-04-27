class Sample:
    z = 0  # static (class) variable

    def __init__(self):
        self.x = 0
        self.y = 0

    def setData(self, x, y, z):
        self.x = x
        self.y = y
        Sample.z = z   # class variable updated

    def display(self):
        print(f"x={self.x}\ty={self.y}\tz={Sample.z}")

    @staticmethod
    def displayShared():
        print(f"Shared data : {Sample.z}")


# Main program
s1 = Sample()
s2 = Sample()
s3 = Sample()

s1.setData(10, 20, 30)
s2.setData(40, 50, 60)
s3.setData(70, 80, 90)

s1.display()
s2.display()
s3.display()

Sample.displayShared()