class Binay_heap:
    def __init__(self):
        self.bh=[0]
        self.current_size=0;
    
    def insert(self,k):
        self.bh.append(k)
        self.current_size+=1
        self.per_up()
    

    def per_up(self):
        CI=self.current_size
        PI=CI//2
        while self.bh[CI]<self.bh[PI] and PI>0:
            # swap
            self.bh[CI],self.bh[PI]=self.bh[PI],self.bh[CI]
            CI=PI
            PI=CI//2
    def per_down(self,index):
        PI=CI//2
        CI=self.current_size
        while self.bh[CI]<self.bh[PI] and PI>0:
            # swap
            self.bh[CI],self.bh[PI]=self.bh[PI],self.bh[CI]
            CI=PI
            PI=CI//2

bh=Binay_heap()
bh.insert(45)
bh.insert(8)
bh.insert(4)
bh.insert(1)

print(bh.bh)    

