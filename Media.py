noteA =float(input("Inform the first note: "))
noteB =float(input("inform the second note: "))

#calculateaverage
notefinish = (noteA + noteB) /2

#verification
if notefinish >=7.0:
    print("The average: %.1f - Approved "%notefinish)
else:
    print("The average: %.1f - Disapproved "%notefinish)

