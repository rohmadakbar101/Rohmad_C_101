cubes = [value**3 for value in range(1, 11)]
for number in cubes:
    cube = number**3
    cubes.append(cube)
    
for cube in cubes:
    print(cube)