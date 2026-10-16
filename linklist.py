class node():
    def __init__(self):
        self.__data=""
        self.__pointer=-1
    def getdata(self):
        return self.__data
    def getpointer(self):
        return self.__pointer
    def setdata(self,d):
        self.__data=d
    def setpointer(self,p):
        self.__pointer=p
class linklist():
    def __init__(self,size):
        self.__list=[node() for i in range(size)]
        for i in range(size-1):
            self.__list[i].setpointer(i + 1)
        self.__list.setpointer(-1)    
        self.__freelist=0
        self.__head=-1
    def addnode(self,data):
        if self.__freelist==-1:
            print("no node available")
        else:
            new=self.__freelist
            self.__freelist=self.__list[self.__freelist].getpointer()
            self.__list[new].setdata(data)
            if self.__head==-1:
                self.__head=new
            else:
                current=self.__head
                while self.__list[current].getpointer()!=-1:
                    current=self.__list[current].getpointer()
                self.__list[current].setpointer(new)    
    def remove(self,noderem):
        if self.__head==-1:
            print("list empty")
        else:
            prev=-1
            current=self.__head
            found=False
            while found==False and current!=-1:
                if self.__list[current].getdata()==noderem:
                    found=True
                else:
                    prev=current
                    current=self.__list[current].getpointer()    
            if found==False:
                print("no such node found")
            else:
                if prev==-1: ##prev will be -1 in the case that there is only one node in the list
                    self.__head=-1
                else:
                    self.__list[prev].setpointer(self.__list[current].getpointer())
                temp=self.__freelist
                self.__freelist=current
                self.__list[current].setpointer(temp)
                print("item removed")
    def traverse(self):
        if self.__head==-1:
            print("empty")
        else:
            current=self.__head
            while current!=-1:
                print(self.__list[current].getdata())
                current=self.__list[current].getpointer()
    def search(self,item):
        if self.__head==-1:
            print("empty")
        else:
            found=False
            current=self.__head
            while current!=-1:
                if self.__list[current].getdata()==item:
                    found=True
                current=self.__list[current].getpointer()
        return found    
            
            
            
            
            
            
            
