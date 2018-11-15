#double_list = ["1","2","3"]
#
#double_list.insert(0, "4")
#
#print(double_list)
class DoubleList:
    def __init__(self, size_of_list):
        self.thelist = ["None"] * (size_of_list-1)

    def setAt(self, index, value):
        self.thelist.insert(index, value)
    
    def __str__(self):
        return ' '.join(self.thelist)

    def __add__(self, other):
        newlist = self.thelist + other.thelist
        return ' '.join(newlist)

def main():
    newlist = DoubleList(3)
    oldlist = DoubleList(2)
    newlist.setAt(2,"bob")
    newlist.setAt(3,"joe")
    oldlist.setAt(0,"steve")
    oldlist.setAt(1,"greg")
    addlist = newlist + oldlist
    print(addlist)

main()