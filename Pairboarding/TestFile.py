def average_damage(dam):
    total = 0
    for num in dam:
        total += num
    print(total / len(dam))
    return total / len(dam)
nums = [5,14,16,4,3,4,2,16,3,15,14,0,4,2,12,14,3,11,15,9,
        4,13,6,1,6,4,1,5,11,4,12,2,3,8,8,14,9,7,4,0,9,5,
        10,0,8,10,0,2,1,10,0,3,4,4,1,7,8,0,3,7,7,12,4,11]

average_damage(nums)
