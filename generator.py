import random
import string 

length = int(input("Password length :"))

chars = string.ascii_length_letters + string.digits
password = "".join(random.choice()for _ in range(length))

print("Password:", password)
