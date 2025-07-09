add1 = "Sahakar Bhavan Sub PostOffice,10th Floor,RCityMallLal BahadurShastriMargGhatkopar WestMumbaiSuburban"

# Split the string by commas
parts = add1.split(',')

result = ""
for part in parts:
    print(len(result))
    print(len(part))
    if len(result) + len(part) + 1 >= 100:  # +1 for the comma
        break
    if result:
        result += ","
    print(part)
    result += part

print(result)
