class Report:
    def __init__(self, levels):
        self.levels = levels

    def _ordercheck(self):
        asc = False
        desc = False

        for prevlevel, currlevel in zip(self.levels, self.levels[1:]):
            if prevlevel > currlevel:
                desc = True
            elif currlevel > prevlevel:
                asc = True
            else:
                desc = True
                asc = True

        return asc ^ desc

    def _diffcheck(self):
        inrange = True

        for prevlevel, currlevel in zip(self.levels, self.levels[1:]):
            if 1 <= abs(prevlevel - currlevel) <= 3:
                pass
            else:
                inrange = False

        return inrange

    def dampcheck(self):

        for count, ele in enumerate(self.levels):
            self.levels.pop(count)
            if self._ordercheck() and self._diffcheck():
                return True
            else:
                self.levels.insert(count, ele)

        return False

    def safecheck(self):

        return self._ordercheck() and self._diffcheck()


f = open('day2input.txt', 'r')
data = f.read().splitlines()

reports = []
safecount = 0

for item in data:
    reports.append(Report(list(map(int, item.split(' ')))))

for report in reports:
    if report.safecheck():
        safecount += 1
    elif report.dampcheck():
        safecount += 1

print("Safecount is: " + str(safecount))
