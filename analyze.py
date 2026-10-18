with open ("wards.csv", "r") as f:
    lines = f.readlines()
    print ("Number of lines", len(lines))

    # print each line
    # for line in lines:
    #     print (line.strip())  what is the effecct of the .strip?


    # for line in lines:
    #         print (line) 

    # for line in lines [1:]:
    #     parts = line.strip(). split(",")
    #     wards = parts[0]
    #     area_km2 = float(parts[1])
    #     area_hectares = area_km2 * 100
    #     print(wards, "is", area_hectares, "hectares")
        

    # for line in lines [1:]:
    #     parts = line.strip(). split(",")
    #     wards = parts[0]
    #     area_km2 = float(parts[1])
    #     area_hectares = area_km2 * 100
    #     print(wards, "is", round(area_hectares, 1), "hectares") #this rounds the decimal to 1

for line in lines [1:]:
        parts = line.strip(). split(",")
        wards = parts[0]
        area_km2 = float(parts[1])
        if area_km2 > 9:
              size = 'large'

        else:
              size = 'small'
        print (wards, 'is', size)


