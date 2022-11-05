class Tainghe:
    data = []
    def __init__ (self, ID, Name, country, cost, quantity, money):
        self.ID = ID
        self.Name = Name
        self.country = country
        self.cost = cost
        self.quantity = quantity
        self.money = money
    def add(self):
        count = int(input("Nhập số lượng tai nghe vào đây: "))
        for i in range(count):
            infor = {"ID": "", "Name": "", "country": '', "cost": "", "quantity": ""}
            self.ID = int(input("Nhập ID sản phẩm: "))
            infor['ID']=self.ID
            while True:
                self.Name = input('Nhập tên sản phẩm: ')
                if 3 <= len(self.Name) <= 5 and self.Name[0:2] == "TN":
                    infor['Name'] = self.Name
                    self.Name = True
                    break
                else:
                    print("Yêu cầu nhập lại!")
            while True:
                self.country = input("Nhập nước sản xuất: ")
                if self.country == 'Hàn Quốc' or self.country == "Nhật Bản":
                    infor['country'] = self.country
                    self.country = True
                    break
                else:
                    print('Yêu cầu nhập lại!')
            self.cost = int(input("Nhập giá sản phẩm: "))
            infor['cost'] = self.cost
            while True:
                self.quantity = int(input("Nhập số lượng sản phẩm: "))
                if self.quantity >= 3:
                    infor['quantity'] = self.quantity
                    self.quantity = True
                    break
                else:
                    print("Yêu cầu nhập lại")
            self.data.append(infor)
        print("Danh sách sản phẩm là: ")
        for i in self.data:
            print(i)
    def find(self,ID):
        datafind = []
        for i in self.data:
            if i.ID ==ID:
                datafind.append(i)
        return datafind

b = Tainghe
b.add(self=Tainghe)
