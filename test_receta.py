
import re

file1 = open('Barlel.md', 'r')
lines = file1.readlines()
INGREDIENTES = 5
TOTAL_LINES = len(lines)


def test_barlel():
    count = 0
    for line in lines:
        count += 1
        if re.search('## Ingredientes',line):
            break
    nro_materials = 0
    for xline in range(count,TOTAL_LINES):
        if re.search('## (.*?)',lines[xline]):
            break
        nro_materials+= 1
    assert nro_materials==INGREDIENTES

        



