facebook = True
twitter = False
instagram = True

print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")

accounts_count = int(facebook) + int(twitter) + int(instagram)

if accounts_count >= 2:
    print("You are a good influencer!")