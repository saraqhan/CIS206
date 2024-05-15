class Employee:
    def __init__(self, fname="N/A", lname="N/A", joblvl=1, yearlysal=0):
        self.fname = fname
        self.lname = lname
        self.joblvl = joblvl
        self.yearlysal = yearlysal
        self.stbonus = self.calc_stbonus()
        self.ltbonus = self.calc_ltbonus()

    def calc_stbonus(self):
        if self.joblvl == 1:
            return 0.25 * self.yearlysal
        elif self.joblvl == 2:
            return 0.20 * self.yearlysal
        elif self.joblvl == 3:
            return 0.10 * self.yearlysal
        else:
            return 0

    def calc_ltbonus(self):
        return 0.10 * self.yearlysal

    def empdetails(self):
        print("first name:", self.fname)
        print("last name:", self.lname)
        print("job level:", self.joblvl)
        print("yearly salary:", self.yearlysal)
        print("short term bonus:", self.stbonus)
        print("long term bonus:", self.ltbonus)


class Manager(Employee):
    def __init__(self, fname="N/A", lname="N/A", joblvl=1, yearlysal=0, auto="N/A"):
        super().__init__(fname, lname, joblvl, yearlysal)
        self.auto = auto

    def calc_ltbonus(self):
        if self.joblvl == 1:
            return 0.50 * self.yearlysal
        elif self.joblvl == 2:
            return 0.40 * self.yearlysal
        elif self.joblvl == 3:
            return 0.35 * self.yearlysal
        else:
            return 0

    def display_auto(self):
        print("automobile:", self.auto)

manager1 = Manager("john", "doe", 2, 70000, "tesla model s")

manager1.empdetails()
manager1.display_auto()
