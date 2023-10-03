from datetime import datetime, timedelta

unuudur = datetime.now()

print("Enter your date of birth (YYYY-MM-DD):")
bday1 = input()

bday2 = datetime.strptime(bday1, "%Y-%m-%d")

nas1 = unuudur - bday2

nas2 = nas1.days // 365

print(f"You are {nas2} years old.")