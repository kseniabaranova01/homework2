ecxponatovEveryDay = (60/5)*8
ecxponatovEveryYear = ecxponatovEveryDay*365
age = 0
while age < 120:
    age += 1
    print(age, " => ", ecxponatovEveryYear*age)
ecxponatovatall = 4204800 + 35040
ages = ecxponatovatall // ecxponatovEveryYear
print("ages=", ages)
