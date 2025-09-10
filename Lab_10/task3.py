

# Corrected class definition with proper __init__ method name and improved formatting
class emp:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def inc(self, p):
        self.s = self.s + (self.s * p / 100)

    def pr(self):
        print("emp:", self.n, "salary:", self.s)

e1 = emp("Alice", 50000)
e1.pr()
e1.inc(10)
e1.pr()
