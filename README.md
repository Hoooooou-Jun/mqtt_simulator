# MQTT simulator program
This simulator is used by ES-Guardians for MQTT message load testing.

There are 4 functions.

1. Manually transmitting emergency situations(Message)
2. Transmit emergency situation to random coordinates within radius
3. Transmit emergency situation with JSON file
4. Extract JSON file included random coordinates within radius

The source was written in ENG, but user prompt was written for korea

## Manual
first, you need to pull source this repository

__REQUIREMENT__
1. It is recommended to use it in a "PyCharm"
2. you need python interpreter version 3.10 or higher
3. you will access virtual environment as "venv"
4. you will enter "pip install -r requirements.txt"

Next, get start your program, you will see a prompt like this:

![Screenshot 2024-01-02 at 3 32 07 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/571c9dac-5406-4ff8-8a62-ce93d363110a)

enter number, you will select functions. 

### 1. Manually transmitting emergency situations(Message)
There are function that transmit emergency situation to own device as coordinates.

if you enter number 1, you will access ***Manually transmitting emergency situations***

![Screenshot 2024-01-02 at 4 23 40 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/6a9c9f05-cf21-4927-aeb3-26f6d948b059)

enter your device name(PA000009, MA000009... __However, you can only enter registered devices.__), latitude, longitude you want to transmit.

if emergency situation was transmitted, you will see a prompt worked normally like this:

![Screenshot 2024-01-02 at 4 29 08 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/be09bab9-e373-4170-b96c-08c97cb27f20)

if an error occurs, will be stopped.

### 2. Transmit emergency situation to random coordinates within radius

This function is the same as function 1, but random coordinate based on center coordinates within radius was transmitted.

if you enter number 2, you can access function.

![Screenshot 2024-01-02 at 4 39 17 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/ce1dbcdb-0aaa-4f2f-94f2-622c508b1eaf)

![Screenshot 2024-01-02 at 4 39 42 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/0900445a-b177-4fe2-8cd1-23856639ce3f)

![Screenshot 2024-01-02 at 4 39 58 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/aa925831-f92e-46aa-b7bf-5d6fe5b4a812)

### 3. Transmit emergency situation with JSON file
This is a function that transmit emergerncy situation by JSON file.

JSON file structured like this:
```json
/* ./dummy.json */
{
  "PA000009": [
    [
      37.594024,
      126.955268
    ],
    [
      37.594036,
      126.955252
    ],
    [
      37.594029,
      126.955255
    ],
    [
      37.594034,
      126.955253
    ],
  ],
  "PA000010": [
    [
      37.594024,
      126.955268
    ],
    [
      37.594036,
      126.955252
    ],
    [
      37.594029,
      126.955255
    ],
    [
      37.594034,
      126.955253
    ],
  ]
}
```
This file was located root directory. file name was written "dummy.json"

If your file is ready, Getting start this function.

![Screenshot 2024-01-02 at 4 41 05 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/14d834af-8b11-42bd-82ad-619c54a72e51)

### 4. Extract JSON file included random coordinates within radius

Like function number 2, you will get random coordinates within radius to JSON file.

This file can be used in function 3.

![Screenshot 2024-01-02 at 4 51 55 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/41034db5-3d1a-4454-9709-4dcb884d4b9f)



## Caution

If the following error occurs, just run the program again.

![Screenshot 2024-01-02 at 4 36 14 PM](https://github.com/Hoooooou-Jun/mqtt_simulator/assets/84234490/df8a718e-7dda-459a-bd6a-237ca1313354)
