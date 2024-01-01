import math
import random

def random_coordinate(latitude, longitude, distance, count):
    coordinate = []

    for _ in range(count):
        # Generate random angle(direction)
        angle = random.uniform(0, 2 * math.pi)

        # Generate random distance
        radius = random.uniform(0, distance)

        # Calculate coordinate using Haversine formula
        cal_latitude = math.degrees(radius / 6371.0)
        cal_longitude = math.degrees(radius / (6371.0 * math.cos(math.radians(latitude))))

        # Add random distance within fixed radius
        res_latitude = round(latitude + cal_latitude * math.sin(angle), 6)
        res_longitude = round(longitude + cal_longitude * math.cos(angle), 6)

        coordinate.append((res_latitude, res_longitude))
    return coordinate
