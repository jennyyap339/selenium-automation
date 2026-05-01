import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "LoginData"

# Add headers
sheet.append(["username", "password", "expected", "should_pass", "skip"])

# Add test data
sheet.append(["tomsmith", "SuperSecretPassword!", "secure area", True, False])
sheet.append(["tomsmith", "WrongPassword!", "invalid", False, False])
sheet.append(["wronguser", "wrongpass", "invalid", False, False])
sheet.append(["tomsmith", "short", "invalid", False, True])

# Save the file
workbook.save("data/login_data.xlsx")
print("Excel file created")