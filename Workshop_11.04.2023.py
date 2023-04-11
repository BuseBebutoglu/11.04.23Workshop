class Human():
    name="Buse"
    # built-in 
    def __init__(self,name):
        self.name = name
        print("Bir human instance'ı üretildi.")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer : {self.__name__}"
    def talk(self,sentence):
        name="Ercan"
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

#instance --> örnek
#self --> this 
human1= Human("Buse")
human1.talk("Merhaba")
human1.walk()

human2 = Human("Halit")
human2.name= "Cem"
human2.talk("Selam")
human2.walk()

##### MODULES

import matematik as m #alias(takma isim)
from matematik import topla as toplamaIslemi
print(matematik.topla(10,20))

