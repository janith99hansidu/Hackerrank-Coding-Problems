"""
Given two values, h1 and h2, which represent the starting and ending HowlUnits, 
print a table showing the corresponding MoonUnits for each HowlUnit in that range.
"""
# moon = howl * 0.621371
factor = 0.621371

def howlUnits(start, end):
    # get the max value of the howl unit
    max_howl = end / factor
    
    # all the conversions
    moon_to_howl = []
    
    # add howl to moon 
    for i in range(start + 1, int(max_howl)+1):
        moon_unit = i * factor
        # add to the list
        moon_to_howl.append((moon_unit, i))
    
    # add moon to howl
    for i in range(start, end+1):
        howl_unit = i / factor
        # add to the list
        moon_to_howl.append((i, howl_unit))
    
    moon_to_howl.sort()
    
    # Print header
    print("MoonUnits    HowlUnits")
    print("-------------------------")
    
    # Print each MoonUnit and HowlUnit pair in the required format
    for moon, howl in moon_to_howl:
        print(f"{moon: .4f}      {howl: .4f}")
    
if __name__ == "__main__":
    start, end = map(int, input().split())
    howlUnits(start, end)
