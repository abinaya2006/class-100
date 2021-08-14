class Car:
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
    
    def start(self):
        print("The car has started")
    
    def stop(self):
        print("The car has stopped")

    def accelerate(self):
        print("Accelerating...")

    def change_gear(self,gear_type):
        print("Gear changed to ",gear_type)
        

nexon=Car("nexon" , "black" , "Tata" , "250")

print(nexon.color)
nexon.start()
nexon.accelerate()
nexon.change_gear("4")
nexon.stop()

