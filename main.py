import os
class Car:
    def __init__(self, model):
        self.model = model
        self.benzin_holati = 100

    def __str__(self):
        return f'Car {self.model}'

    def mash_ot_oldirish(self):
        print("Engine is on")

    def mash_ochirish(self):
        uuu = ['3']
        print("Engine is off")
        print(f"""
                    {self.__str__()}

                    1. Engine on
                    2. Engine off
                    3. Go to....
                    4. Fill petrol
                    5. View status
                    6. Exit
                            """)

        n = input(">>>").strip()
        while n in uuu:
            print("Engine is off")
            print(f"""
                                {self.__str__()}

                                1. Engine on
                                2. Engine off
                                3. Go to....
                                4. Fill petrol
                                5. View status
                                6. Exit             """)
            n = input(">>>>")

        self.pri()

    def masofaga_borish(self):
        n = int(input("Enter ditanse km - >>>").strip())
        if n >= 1 and n <= self.benzin_holati:
            self.benzin_holati -= n
            print("Destination reached")
        else:
            print("No petrol")

    def benzin_toldirish(self):
        n = int(input("Amount >>>>").strip())
        if self.benzin_holati + n <= 100:
            self.benzin_holati += n
            print(f"Full tank {self.benzin_holati} + {n}")
        else:
            print("Full tank --- 100 petrol left unused")

    def mash_holati(self):
        print(f"{self.benzin_holati}")

    def pri(self):
        lis = ['1', '2', '3', '4', '5', '6']
        while True:
            print(f"""
                   {self.__str__()}

                    1. Engine on
                    2. Engine off
                    3. Go to....
                    4. Fill petrol
                    5. View status
                    6. Exit
                    """)

            n = input(">>>").strip()
            while n not in lis:
                print("Xato kiritingiz:")
                os.system("clear")
                n = input(">>>>").strip()

            if n == lis[0]:
                self.mash_ot_oldirish()
            elif n == lis[1]:
                self.mash_ochirish()
            elif n == lis[2]:
                self.masofaga_borish()
            elif n == lis[3]:
                self.benzin_toldirish()
            elif n == lis[4]:
                self.mash_holati()
            else:
                print("-------Godbye-------")
                exit()

    def start(self):
        lis = ['1', '2']
        print("""
                Start [1]
                Exit  [2]

        """)
        n = input(">>>>").strip()
        while n not in lis:
            n = input("Xato kiritingiz: >>>>")
            # os.system("clear")
        if n == lis[0]:
            print('\nThe car is off <--')
            self.pri()
        elif n == lis[1]:
            print("-------------Godbye--------------")


car1 = Car('Audi')
car1.start()
