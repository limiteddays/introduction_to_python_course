class human:

    def __init__(self, name, age, location, occ):
        self.name = name
        self.age = age
        self.location = location
        self.occ = occ


    def restaurant_check(self):

        if self.age < 10:
            print("baby price")

        elif self.age < 19:
            print("student price")

        else:
            print("adult price")



if __name__ == '__main__':

    kun = human("kun", 21, "waitara", "USYD student")

    print(kun.age)

    kun.restaurant_check()
