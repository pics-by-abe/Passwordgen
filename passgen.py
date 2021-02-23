import secrets
import string as s

length = int(input("Passwordlength: "))


chars = s.ascii_letters + s.digits + s.punctuation


print("".join(secrets.choice(chars) for _ in range(length)))