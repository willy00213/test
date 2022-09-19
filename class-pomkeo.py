#1建立Pokemon的類別
#2設定初始狀態
#3設計方法(ex..attack,defence,cure.showinfo)
class Pokemon:
    ct =0   #類別屬性 共用的
    def __init__(self,name,lv=1,hp=15):
        self.name = name
        self.lv = lv
        self.hp = hp
        self.hpmax = hp
        Pokemon.ct +=1           #有幾隻
    def  attack(self,target):
            if self.hp>0:
                print(self.name,'攻擊'+target.name)
                target.defence(self.lv)
            else :
                print(self.name,'死了')
        
    def  defence(self,att):
            self.hp -= att
            if self.hp <= 0:
                self.hp = 0
                print(self.name,"死了")
            else:
                    print(self.name,'受到%d攻擊'%(att))

    def  cure(self):
            self.hp =  self.hpmax
            print(self.name,'滿血!!')
        
    def  showinfo(self):
            print('Name:',self.name,'[lv:%d hp:%d /%d]'%(self.lv,self.hp, self.hpmax))

p1 = Pokemon('皮卡丘',lv=4)
p1.showinfo()
p2 = Pokemon('傑尼龜',lv=5, hp=40)
p2.showinfo()
p3 = Pokemon("小火龍", lv=10, hp=50)
p3.showinfo()
print('總共有：',Pokemon.ct)
p1.attack(p3)
p3.showinfo()
p1.attack(p3)
p1.attack(p3)
p3.cure()
