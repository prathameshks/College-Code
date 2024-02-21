
# Generate data
import random
import string
import pandas as pd

# Define first names
first_names = ["Aakash", "Anika", "Arjun", "Deepika", "Divya", "Rahul", "Nikita", "Rishi", "Priyanka", "Manish",
               "Ananya", "Rohan", "Pooja", "Karan", "Shruti", "Suresh", "Vaishnavi", "Vikram", "Seema", "Amit"]

# Define last names
last_names = ["Singh", "Kumar", "Sharma", "Devi", "Patel", "Khan", "Gupta", "Yadav", "Das", "Rao",
               "Mehta", "Jha", "Chauhan", "Verma", "Pandey", "Trivedi", "Nair", "Agarwal", "Mittal", "Bose"]

# Create roll numbers
roll_numbers = [random.randint(1, 1000) for _ in range(50)]

# Generate mobile numbers
def generate_mobile_number():
  country_code = "+91"
  mobile_number_start = random.choice(["7", "8", "9"])
  remaining_digits = "".join([random.choice(string.digits) for _ in range(9)])
  return country_code + mobile_number_start + remaining_digits

mobile_numbers = [generate_mobile_number() for _ in range(50)]

# Generate first and second CGPA
def generate_cgpa():
  return round(random.uniform(0, 10), 2)

first_cgpa = [generate_cgpa() for _ in range(50)]
second_cgpa = [generate_cgpa() for _ in range(50)]

# Create dataframe
data = {
    "Roll Number": roll_numbers,
    "First Name": [random.choice(first_names) for _ in range(50)],
    "Last Name": [random.choice(last_names) for _ in range(50)],
    "Mobile Number": mobile_numbers,
    "First Semester CGPA": first_cgpa,
    "Second Semester CGPA": second_cgpa
}


df = pd.DataFrame(data)

# save as data.csv
df.to_csv('data.csv', index=False)


