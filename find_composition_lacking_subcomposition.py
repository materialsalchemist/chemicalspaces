from pymatgen.core import Structure
import json
import itertools
f = open("C:/MyDatasets/MP.json")
MP = json.load(f)
f.close()
print("Loaded")
compositions = []
missing = {}
for m in MP:
    if len(set(m["elements"])) == 4:
        minus_what = 1
        chem_space = list(set(m["elements"]))
        chem_spaces_minus_1 = itertools.combinations(chem_space, len(chem_space) - minus_what)
        for chem_space_minus_1 in chem_spaces_minus_1:
            found = False
            for mm in MP:
                if len(set(mm["elements"])) != len(chem_space_minus_1):
                    continue
                if set(mm["elements"]) == set(chem_space_minus_1):
                    found = True
                    break
            if not found:
                print(chem_space_minus_1, "not found for", chem_space)
                k = '_'.join(list(sorted(chem_space)))
                if k in missing:
                    missing[k] += [chem_space_minus_1]
                else:
                    missing[k] = [chem_space_minus_1]
f = open('missing.json','w')
json.dump(missing,f)
f.close()