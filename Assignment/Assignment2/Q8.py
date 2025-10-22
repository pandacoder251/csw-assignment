emails = ["test@gmail.com","hello123","abc.org","world@yahoo.com"]

# a) Filter valid emails
valid_emails = list(filter(lambda e: '@' in e and (e.endswith(".com") or e.endswith(".org")), emails))
print("Valid Emails:", valid_emails)

# b) Extract domain names
domains = [e.split('@')[1].split('.')[0] for e in valid_emails]
print("Domains:", domains)

# c) Frequency dictionary for domains
domain_freq = {d: domains.count(d) for d in set(domains)}
print("Domain Frequency:", domain_freq)
