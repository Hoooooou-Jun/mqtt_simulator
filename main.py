import os
import time
from dotenv import load_dotenv
from src import mqtt
from src.random_coordinate import random_coordinate
from src.read_json import read_json
from src.extract_json import extract_json

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

load_dotenv()

# Set your MQTT client name & topic
mqtt_instance = mqtt.Mqtt('MqttSimulator', 'local')
mqtt_connection = mqtt_instance.mqttConnection()
mqtt_instance.connectMqtt(mqtt_connection)

def main():
    print("====================================================")
    print("====================================================")
    print("===============MQTT simulator program===============")
    print("====================================================")
    print("====================================================")
    time.sleep(2)
    print("1. 비상상황 수동 전송하기")
    print("2. 반경 내 랜덤 좌표로 비상상황 전송하기")
    print("3. JSON 파일로 비상상황 전송하기")
    print("4. 랜덤 좌표 JSON 파일 추출하기")
    print("\n")
    select = int(input("사용하실 기능의 번호를 입력해주세요. : "))

    if select == 1:
        clear()
        print("====================================================")
        print("==================비상상황 수동 전송하기==================")
        print("====================================================")
        temId = input("기기명을 입력해주세요. : ")
        lat = input("위도를 입력해주세요. : ")
        lng = input("경도를 입력해주세요. : ")
        print(f'3초 뒤 {temId} 기기로 {lat}, {lng} 좌표에 비상상황을 전송합니다.')
        time.sleep(3)

        clear()
        mqtt_instance.sendMqttMessage(mqtt_connection, temId, lat, lng)
        print("비상상황 수동 전송이 완료되었습니다.")
        print("3초 뒤 메인화면으로 돌아갑니다.")
        time.sleep(3)
        main()
    elif select == 2:
        clear()
        print("=====================================================")
        print("=============반경 내 랜덤 좌표로 비상상황 전송하기=============")
        print("=====================================================")
        temId = input("기기명을 입력해주세요. : ")
        lat = input("기준 위도를 입력해주세요. : ")
        lng = input("기준 경도를 입력해주세요. : ")
        distance = int(input("반경을 입력해주세요(km / ex: 5, 10). : "))
        count = int(input("비상상황 전송 숫자를 입력해주세요. : "))
        print(f'3초 뒤 {temId} 기기로 중심 좌표 {lat}, {lng} 기준 {distance}km 거리 내 랜덤으로 비상상황 {count}번 전송합니다.')
        print("비상상황은 2초 간격으로 전송됩니다.")

        res_random_coordinate = random_coordinate(lat, lng, distance, count)
        time.sleep(3)

        for idx, coord in enumerate(res_random_coordinate, start=1):
            clear()
            print(f"위도: {coord[0]}, 경도: {coord[1]}")
            print(f"{temId} 기기로 비상상황을 전송합니다.")
            print(f"[현재 순회: {idx}/{len(res_random_coordinate)}]")
            mqtt_instance.sendMqttMessage(mqtt_connection, temId, coord[0], coord[1])
            print("2초 뒤 다음 비상상황이 전송됩니다.")
            time.sleep(2)

        print("반경 내 랜덤 좌표로 비상상황 전송이 완료되었습니다.")
        print("3초 뒤 메인화면으로 돌아갑니다.")
        time.sleep(3)
        main()
    elif select == 3:
        clear()
        print("====================================================")
        print("===============JSON 파일로 비상상황 전송하기===============")
        print("====================================================")
        data = read_json().items()
        device_count = 0
        message_count = 0

        for key, value in data:
            print(f"{key} 기기 확인")
            device_count = device_count + 1
            for _ in value:
                message_count = message_count + 1
        print(f"{device_count}대의 기기에서 {message_count}개의 데이터가 확인되었습니다.")
        select = int(input("비상상황을 전송하시겠습니까?(yes: 1/no: 0) : "))
        if select:
            print(f'3초 뒤 ./dummy.json 경로의 데이터로 비상상황을 전송합니다.')
            print("비상상황은 2초 간격으로 전송됩니다.")
            time.sleep(3)

            for key, value in data:
                clear()
                print(f"{key} 기기로 비상상황을 전송합니다.")
                print(f"{len(data)}대 중 {key}대 전송중입니다.")
                for idx, coord in enumerate(value, start=1):
                    print(f"[현재 순회: {idx}/{len(value)}]")
                    mqtt_instance.sendMqttMessage(mqtt_connection, key, coord[0], coord[1])
                    print("2초 뒤 다음 비상상황이 전송됩니다.")
                    time.sleep(2)
                print("3초 뒤 다음 기기에서 비상상황이 전송됩니다.")
                time.sleep(3)

            print("JSON 파일로 비상상황 전송이 완료되었습니다.")
            print("3초 뒤 메인화면으로 돌아갑니다.")
            time.sleep(3)
            main()
        else:
            print("3초 뒤 메인화면으로 돌아갑니다.")
            time.sleep(3)
            main()
    elif select == 4:
        clear()
        print("====================================================")
        print("===============랜덤 좌표 JSON 파일 추출하기===============")
        print("====================================================")
        temId = input("기기명을 입력해주세요. : ")
        lat = input("기준 위도를 입력해주세요. : ")
        lng = input("기준 경도를 입력해주세요. : ")
        distance = int(input("반경을 입력해주세요(km / ex: 5, 10). : "))
        count = int(input("비상상황 전송 숫자를 입력해주세요. : "))
        print(f'3초 뒤 {temId} 기기로 중심 좌표 {lat}, {lng} 기준 랜덤 좌표 비상상황 JSON 파일이 추출됩니다.')
        print("해당 파일은 ./output.json 경로에 저장됩니다.")
        time.sleep(3)

        coord_data = random_coordinate(lat, lng, distance, count)
        extract_json(temId, coord_data)

        print("랜덤 좌표 JSON 파일 추출이 완료되었습니다.")
        print("3초 뒤 메인화면으로 돌아갑니다.")
        time.sleep(3)
        main()
    else:
        print("잘못된 입력입니다.")

main()
