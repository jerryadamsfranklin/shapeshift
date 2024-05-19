import myfitnesspal
from datetime import date
import pandas as pd

def get_fitness_stats(input_date):
    # Create a MyFitnessPal client
    client = myfitnesspal.Client()

    # Fetch diary for the given date
    day = client.get_date(input_date.year, input_date.month, input_date.day)

    # Calories consumed from food (total calories from all meals)
    total_calories_consumed = day.totals['calories']

    # Macronutrient intake
    carbohydrates = day.totals['carbohydrates']
    fat = day.totals['fat']
    protein = day.totals['protein']
    sodium = day.totals['sodium']
    sugar = day.totals['sugar']

    # Calories burned from walking
    calories_burned = day.exercises[0].get_as_list()[0]['nutrition_information']['calories burned']

    # Today's weight
    weight = client.get_measurements('Weight')
    weight_numbers = weight[input_date]

    # Return the results
    return {
        "Date": input_date.strftime("%Y-%m-%d"),
        "Calories Consumed": total_calories_consumed,
        "Carbohydrates": carbohydrates,
        "Protein": protein,
        "Fat": fat,
        "Sodium": sodium,
        "Sugar": sugar,
        "Calories Burned": calories_burned,
        "Weight": weight_numbers
    }

# Example usage:
input_date = date(2024, 4, 23)  # Change to the desired date
results = get_fitness_stats(input_date)

# Create a DataFrame
df = pd.DataFrame([results])

# Display the DataFrame
print(df)
