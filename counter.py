class Counter:
    count=0

    def __init__(self): #init constructor method hai jo har baar call hota hai jab hum Counter class ka naya object banate hain.
        Counter.count+=1

    @classmethod  #@classmethod decorator hai jo display_count method ko class method banata hai.
    def display_count(cls):
         #cls parameter hai jo class (Counter) ko represent karta hai.
        print(f"Total Object created: {cls.count}")


c1= Counter()
c2 = Counter()
c3 = Counter()
Counter.display_count()