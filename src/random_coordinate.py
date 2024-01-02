import math
import random

def random_coordinate(latitude, longitude, distance, count):
    coordinates = []
    lat_radian = math.radians(float(latitude))
    lon_radian = math.radians(float(longitude))

    for _ in range(int(count)):
        earth_radius = 6371.0

        # Generate random angle(direction)
        angle = random.uniform(0, 2 * math.pi)

        # Generate random distance
        radius = random.uniform(0, distance)

        # Calculate coordinate using Haversine formula
        cal_latitude = math.asin(math.sin(lat_radian) * math.cos(radius / earth_radius) + math.cos(lat_radian) * math.sin(distance / earth_radius) * math.cos(angle))
        cal_longitude = lon_radian + math.atan2(math.sin(angle) * math.sin(radius / earth_radius) * math.cos(lat_radian),
                                                     math.cos(radius / earth_radius) - math.sin(lat_radian) * math.sin(cal_latitude))

        # Convert radian to degrees
        res_latitude = round(math.degrees(cal_latitude), 6)
        res_longitude = round(math.degrees(cal_longitude), 6)

        coordinates.append((res_latitude, res_longitude))

    return coordinates
