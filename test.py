import myfitnesspal

client = myfitnesspal.Client()
# client = myfitnesspal.Client('jerryadamsf', 'carter6333')


day = client.get_date(2024, 4, 24)
print(day)
