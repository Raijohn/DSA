class Pencil:
    #class variable same for all objects
    catagory = "starionery"

    #construtor
    def __init__(self,color,length,thickness):
        #instans variables diffrent for every object
        self.color = color
        self.length = length
        self.thickness = thickness
    def sharpen(self):
        self.length = self.length - 0.2

pencil1 = Pencil("red",10,2)

print(pencil1.color)
print(pencil1.length)
print(pencil1.thickness)
print(pencil1.catagory)
pencil1.sharpen()
print(pencil1.length)

pencil2 = Pencil("blue",12,8)

print(pencil2.color)
print(pencil2.length)
print(pencil2.thickness)
print(pencil2.catagory)