# # variables 
# distance_mi = 5
# is_raining = True
# has_bike = True
# has_car = True
# has_ride_share_app = True

# if distance_mi == 0:
#     print(False)
# elif distance_mi <= 1 and is_raining == False:
#     print(True)
# elif distance_mi <= 1 and is_raining == True:
#     print(False)
# elif distance_mi > 1 and distance_mi <= 6 and is_raining == True and has_bike == False:
#     print(False)
# elif distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == False:
#     print(False)
# elif distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == True:
#     print(True)
# elif distance_mi > 6 and has_ride_share_app == True:
#     print(True)
# elif distance_mi > 6 and has_car == True:
#     print(True)
# elif distance_mi > 6 and has_car == False and has_ride_share_app == False:
#     print(False)
# else:
#     print(True)



# Cleaned
distance_mi = 5
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi == 0:
    print(False)
elif distance_mi <= 1:
    if is_raining == False:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if is_raining == True and has_bike == False:
        print(False)
    elif is_raining == False and has_bike == False:
        print(False)
    else:
        print(True)
elif distance_mi > 6:
    if has_ride_share_app == True:
        print(True)
    elif has_car == True:
        print(True)
    else:
        print(False) # no car no ride share
else:
    print(True)
