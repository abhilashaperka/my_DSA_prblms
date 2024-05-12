def trapped_rain_water(elevation_map):
    water = 0
    n = len(elevation_map)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = elevation_map[0]
    right_max[n - 1] = elevation_map[n - 1]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], elevation_map[i])
    
    for j in range(n - 2, -1, -1):
        right_max[j] = max(right_max[j + 1], elevation_map[j])
    
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - elevation_map[i])
    
    return water

def test_trapped_rain_water():
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),  
        ([4,2,0,3,2,5], 9),                
        ([3,1,2,4,0,1,3,2,1,4,2,1,0,1,3], 21)  
    ]
    
    for elevation_map, expected in test_cases:
        result = trapped_rain_water(elevation_map)
        if result == expected:
            print(f"Pass for {elevation_map}. Trapped water: {result}")
        else:
            print(f"Fail for {elevation_map}. Expected: {expected}, but got: {result}")


test_trapped_rain_water()


