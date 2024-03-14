import json

def edit_orgs(num, input):
    # Note from greenturtle537 (Owner)
    # Your function has spoiled. Complaing about string indices must be integers in logs.
    # I pass num as an "int" and input as a whatever Vincent did.
    with open("orgs.json") as f:
        orgs = json.load(f)
    for key in input:
        if key != 'contact':

            orgs[num-1][key] = input[key]
        else:
            for subkey in input[key]:
                orgs[num-1][key][subkey] = input[key][subkey]
    
    out = {'organizations': orgs}
        
    with open("test/orgs_testing.json", "w") as outfile:
        outfile.write(json_out)

# example function usage below
"""
num = 15
input = {'name': "HealthcareLast Clinics", 'contact': {'name': "Bro Bro XXIV"}}

edit_orgs(num, input)

with open("test/orgs_testing.json") as f:
    orgs = json.load(f)['organizations']
    
    print(f"orgs: {orgs[14]}")
"""
