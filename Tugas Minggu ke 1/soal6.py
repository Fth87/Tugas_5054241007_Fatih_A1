#Predict score on final exam

desiredGrade = input('Enter desired grade > ')
minAvg = float(input('Enter minimum average required > '))
currentAvg = float(input('Enter current average in course > '))
finalPercentage = float(input('Enter how much the final counts as a percetage of the course grade > '))

finalPercentage /= 100
secondaryPercentage = 1 - finalPercentage

#currentAvg * secondaryPercentage + needScore * finalPercentage = minAvg
needScore = (minAvg - currentAvg * secondaryPercentage) / finalPercentage

print(f"you need a score of {needScore:.2f} on the final to get a {desiredGrade}")

