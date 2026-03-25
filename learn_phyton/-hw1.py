passwords = ["1g234OP45", "1234577", "123456", "1234567890"]
# for password in passwords:
#     if len(password)>=8:
#         print(password)
new_passwords = list(filter(lambda password: len(password)>=8, passwords))
print(new_passwords)