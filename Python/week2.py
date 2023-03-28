first = {"brother": "Steve", "sister": "Mary", "Father": "Ted"}
last = {"Steve": "Jobs", "Mary": "Stevens", "Ted": "Simmons"}
birth = {"brother": "04-Nov-1964", "mother": "1-Jun-1980", "Father": "18-Dec-1924"}
address = {"brother": "123 Main street", "mother": "543 South Point", "Father": "543 South Point"}

print(first["brother"], last[first["brother"]], birth['brother'], address['brother'])

if 'sister' in first.keys(): print(first["brother"])
if 'sister 2' in first.keys(): print(first["brother 2"])
else:
    print('no sister')
