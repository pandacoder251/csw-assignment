voters = [("Amit",22,"Indian"),("John",30,"USA"),("Neha",17,"Indian"),("Ravi",19,"Indian")]

# a) Extract eligible voters
eligible = list(filter(lambda v: v[1] >= 18 and v[2]=="Indian", voters))
eligible_names = [v[0] for v in eligible]
print("Eligible:", eligible_names)

# b) Count of eligible voters
print("Count:", len(eligible_names))

# c) Dictionary with eligible and not eligible
voter_dict = {
    "Eligible": [v[0] for v in voters if v[1] >= 18 and v[2]=="Indian"],
    "NotEligible": [v[0] for v in voters if not (v[1] >= 18 and v[2]=="Indian")]
}
print(voter_dict) 