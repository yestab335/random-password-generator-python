# Imports
import random

# Variables
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*/><?"

use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 8

password = "".join(random.sample(use_for, length_for_pass))

print("Your generated password is:", password)