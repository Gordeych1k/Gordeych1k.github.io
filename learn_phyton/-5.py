emails = ["bohdan@gmail.com", "1@com", "alex.com", "maria@domain", "test@.com"]
def is_valid_emails(email):
    return "@" in email and "." in email and email.find("@")+1 < email.find(".")


real_emails = list(filter(is_valid_emails, emails))

print(real_emails)