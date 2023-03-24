# bennys_billy_calculator
calculates bills for those annoying housemates that tend to go on holiday a lot


## implementation:

```
if __name__ == '__main__':
    bill = Bill(period=57, cost=140.11)

    habitants = [
        Habitant(name="ben"),#default val for daysAbsentDuringBillingPeriod=0 
        Habitant(name="matty"),
        Habitant(name="james", daysAbsentDuringBillingPeriod=8)
    ]

    Calculator(bill=bill, habitants=habitants).calculateShareOfCost()
```
changes names and figures as needed
