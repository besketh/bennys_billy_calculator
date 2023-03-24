class Habitant:
    name = None
    daysAbsentDuringBillingPeriod = None

    def __init__(self, name, daysAbsentDuringBillingPeriod):
        self.name = name
        self.daysAbsentDuringBillingPeriod = daysAbsentDuringBillingPeriod
        assert name is not None, "name needed"
        assert daysAbsentDuringBillingPeriod is not None, "daysAbsentDuringBillingPeriod needed"


class Bill:
    period = None
    cost = None

    def __init__(self, period, cost):
        self.period = period
        self.cost = cost
        assert period, "period needed"
        assert cost, "cost needed"


class Calculator:
    bill = None
    habitants = None

    def __init__(self, bill, habitants):
        self.bill = bill
        self.habitants = habitants

        assert self.bill is not None, "bill is needed"
        assert type(self.bill) == Bill, "bill must be of type Bill"
        assert type(self.habitants) == list, "habitants must be a list"
        assert self.habitants, "need at least 1 habitant"
        for count, habitant in enumerate(self.habitants, start=1):
            assert type(habitant) == Habitant, "habitant " + str(count) + " is not of type Habitant"

    def calculateTotalDaysSpentInApartmentByEverybody(self):
        totalDaysSpentInApartmentByEverybody = 0
        for habitant in self.habitants:
            assert not habitant.daysAbsentDuringBillingPeriod > self.bill.period, "days absent for habitant " + habitant.name + " is greater than the billing period, this is not possible"
            totalDaysSpentInApartmentByEverybody = totalDaysSpentInApartmentByEverybody + self.bill.period - habitant.daysAbsentDuringBillingPeriod

        if totalDaysSpentInApartmentByEverybody == 0:
            raise Exception("totalDaysSpentInApartmentByEverybody can't be 0")

        print("totalDaysSpentInApartmentByEverybody " + str(totalDaysSpentInApartmentByEverybody) + "\n")
        return totalDaysSpentInApartmentByEverybody

    def calculateShareOfCost(self):
        totalDaysSpentInApartmentByEverybody = self.calculateTotalDaysSpentInApartmentByEverybody()

        print("share of the cost of the €" + str(self.bill.cost) + " bill with a period of " + str(
            self.bill.period) + " days\n")
        for habitant in self.habitants:
            shareOfCost = (self.bill.period - habitant.daysAbsentDuringBillingPeriod) / totalDaysSpentInApartmentByEverybody * self.bill.cost

            print(
                habitant.name + " was absent " + str(habitant.daysAbsentDuringBillingPeriod) + " days and owes €" + str(
                    round(shareOfCost, 2)))


if __name__ == '__main__':
    bill = Bill(period=57, cost=140.11)

    habitants = [
        Habitant(name="ben", daysAbsentDuringBillingPeriod=0),
        Habitant(name="matty", daysAbsentDuringBillingPeriod=0),
        Habitant(name="james", daysAbsentDuringBillingPeriod=8)
    ]

    Calculator(bill=bill, habitants=habitants).calculateShareOfCost()
