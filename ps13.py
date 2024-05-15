class Employee:
    def __init__(self, fname="N/A", lname="N/A", joblvl=1, yearlysal=0):
        self.fname = fname
        self.lname = lname
        self.joblvl = joblvl
        self.yearlysal = yearlysal
        self.stbonus = self.calculate_short_term_bonus()
        self.ltbonus = self.calc_ltbonus()

    def calculate_short_term_bonus(self):
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

employee1 = Employee("john", "doe", 2, 50000)

employee1.empdetails()
