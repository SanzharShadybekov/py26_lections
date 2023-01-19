
# case 1
# path = 8
# steps = 'UDDDUDUU'
# result = 1 dolina

# case2
# path = 10
# steps = 'DUDDDUUDUU'
# result = 2 dolina


path = 'UUUDDDUDUD'
steps = 8

sea_level = 0
valleys = 0
for step in steps:
    if step == 'U':
        sea_level += 1
        if sea_level == 0:
            valleys += 1
    elif step == 'D':
        sea_level -= 1

print(f'Result: {valleys} count!')

