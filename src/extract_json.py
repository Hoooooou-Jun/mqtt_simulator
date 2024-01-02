import json
def extract_json(device_id, coordinate):
    output_data = {device_id: []}

    # add coordinate at data
    for coord in coordinate:
        output_data[device_id].append([round(coord[0], 6), round(coord[1], 6)])

    # Output JSON file
    with open('output.json', 'w') as file:
        json.dump(output_data, file, indent=2)
