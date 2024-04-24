import myfitnesspal
from datetime import datetime
from datetime import date

client = myfitnesspal.Client()

# Get today's date
today = datetime.now()

# Fetch today's diary
day = client.get_date(today.year, today.month, today.day)

# Calories consumed from food (total calories from all meals)
total_calories_consumed = day.totals['calories']
print("Calories Coinsumed = ", total_calories_consumed)

#macronutirent intake
print("Macronutirent intake : ", day.totals)

#caloreis burned from walking
print("Calories Burned = ", day.exercises[0].get_as_list()[0]['nutrition_information']['calories burned'])

#today's weight
weight = client.get_measurements('Weight')
today_weight = weight[date.today()]
print("Today's Weight", today_weight)

# Log out from MyFitnessPal
# client.logout()
