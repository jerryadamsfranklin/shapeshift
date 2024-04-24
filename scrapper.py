import myfitnesspal

client = myfitnesspal.Client()

day = client.get_date(2024, 4, 24)
print(day)
