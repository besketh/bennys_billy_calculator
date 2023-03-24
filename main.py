class Habitant:
    name = None
    daysAbsentDuringBillingPeriod = None

    def __init__(self, name, daysAbsentDuringBillingPeriod):
        assert type(name) == str, "name string needed"
        assert type(daysAbsentDuringBillingPeriod) in [type(2), type(
            2.2)], "daysAbsentDuringBillingPeriod of numeric type needed: no symbols, decimals ok"
        assert daysAbsentDuringBillingPeriod >= 0, "can't have negative days absent"

        self.name = name
        self.daysAbsentDuringBillingPeriod = daysAbsentDuringBillingPeriod


class Bill:
    period = None
    cost = None

    def __init__(self, period, cost):
        assert type(period) in [type(2), type(2.2)], "period of numeric type needed: no symbols, decimals ok"
        assert type(cost) in [type(2), type(2.2)], "cost of numeric type needed: no symbols, decimals ok"
        assert period > 0, "period must be greater than 0"
        assert cost > 0, "cost must be greater than 0"

        self.period = period
        self.cost = cost


class Calculator:
    bill = None
    habitants = None

    def __init__(self, bill, habitants):
        assert type(bill) == Bill, "bill must be of type Bill"
        assert type(habitants) == list, "habitants must be a list"
        assert habitants, "need at least 1 habitant"
        for count, habitant in enumerate(habitants, start=1):
            assert type(habitant) == Habitant, "habitant " + str(count) + " is not of type Habitant"

        self.bill = bill
        self.habitants = habitants

    def calculateTotalDaysSpentInApartmentByEverybody(self):
        totalDaysSpentInApartmentByEverybody = 0
        for habitant in self.habitants:
            assert not habitant.daysAbsentDuringBillingPeriod > self.bill.period, "days absent for habitant " + habitant.name + " is greater than the billing period, this is not possible"
            totalDaysSpentInApartmentByEverybody = totalDaysSpentInApartmentByEverybody + self.bill.period - habitant.daysAbsentDuringBillingPeriod

        assert not totalDaysSpentInApartmentByEverybody == 0, "totalDaysSpentInApartmentByEverybody can't be 0"

        print("totalDaysSpentInApartmentByEverybody " + str(totalDaysSpentInApartmentByEverybody) + "\n")
        return totalDaysSpentInApartmentByEverybody

    def calculateShareOfCost(self):
        totalDaysSpentInApartmentByEverybody = self.calculateTotalDaysSpentInApartmentByEverybody()

        print("share of the cost of the €" + str(self.bill.cost) + " bill with a period of " + str(
            self.bill.period) + " days\n")
        for habitant in self.habitants:
            shareOfCost = (
                                      self.bill.period - habitant.daysAbsentDuringBillingPeriod) / totalDaysSpentInApartmentByEverybody * self.bill.cost

            print(
                habitant.name + " was absent " + str(habitant.daysAbsentDuringBillingPeriod) + " days and owes €" + str(
                    round(shareOfCost, 2)))


if __name__ == '__main__':
    bill = Bill(period=57, cost=140.11)

    habitants = [
        Habitant(name="ben", daysAbsentDuringBillingPeriod=0),
        Habitant(name="matty", daysAbsentDuringBillingPeriod=0),
        Habitant(name="james", daysAbsentDuringBillingPeriod=0)
    ]

    Calculator(bill=bill, habitants=habitants).calculateShareOfCost()
