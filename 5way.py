# 교과목명: 창업연계공학설계입문
# 작성자: 김상철
# 일자: 2017 년 9월 28 일
# 내 용: 5방향 추적센서의 데이터를 입력받아, 데이터를 터미널에 출력하기

import RPi.GPIO as GPIO # import GPIO librery
import time # 시간 모듈
from time import sleep # sleep 함수 사용위해 time module import함

GPIO.setmode(GPIO.BOARD)  # Board Mode and BCM Mode

# Vcc = 1 # # Raspberry Pi GPIO 1 번과 연결
OTD = 16  # Raspberry Pi GPIO 16 번과 연결
OTB = 18  # Raspberry Pi GPIO 18 번과 연결
OTA = 22  # Raspberry Pi GPIO 22 번과 연결
OTC = 40  # Raspberry Pi GPIO 40 번과 연결
OTE = 32  # Raspberry Pi GPIO 32 번과 연결

GPIO.setup(OTD, GPIO.IN)  # OTD에서 오는 데이터를 Raspberry Pi GPIO 16번 핀 입력으로 받음
GPIO.setup(OTB, GPIO.IN)  # OTB에서 오는 데이터를 Raspberry Pi GPIO 18번 핀 입력으로 받음
GPIO.setup(OTA, GPIO.IN)  # OTA에서 오는 데이터를 Raspberry Pi GPIO 22번 핀 입력으로 받음
GPIO.setup(OTC, GPIO.IN)  # OTC에서 오는 데이터를 Raspberry Pi GPIO 40번 핀 입력으로 받음
GPIO.setup(OTE, GPIO.IN)  # OTE에서 오는 데이터를 Raspberry Pi GPIO 32번 핀 입력으로 받음

try: # 예외처리 구문, 평상시에는 (while True) print()를 사용하여 센서값을 출력함
    while True:
       print("OTD: " + str(GPIO.input(OTD)))  # OTD에서 오는 데이터를 Raspberry Pi GPIO 16번 핀 입력으로 받음(input), input()함수 리턴 (0, 1)은 str()임으로 int()로 변환
       print("OTB: " + str(GPIO.input(OTB)))  # OTB에서 오는 데이터를 Raspberry Pi GPIO 18번 핀 입력으로 받음(input), input()함수 리턴 (0, 1)은 str()임으로 int()로 변환
       print("OTA: " + str(GPIO.input(OTA)))  # OTA에서 오는 데이터를 Raspberry Pi GPIO 22번 핀 입력으로 받음(input), input()함수 리턴 (0, 1)은 str()임으로 int()로 변환
       print("OTC: " + str(GPIO.input(OTC)))  # OTC에서 오는 데이터를 Raspberry Pi GPIO 40번 핀 입력으로 받음(input), input()함수 리턴 (0, 1)은 str()임으로 int()로 변환
       print("OTE: " + str(GPIO.input(OTE)))  # OTE에서 오는 데이터를 Raspberry Pi GPIO 32번 핀 입력으로 받음(input), input()함수 리턴 (0, 1)은 str()임으로 int()로 변환
       sleep(2)  # Print()한 내용을 2초간 디스플레이 함
               
except KeyboardInterrupt: # 예외처리 구문, Ctrl+C가 눌려지면 cleanup()함수를 통해 GPIO값을 받지 않음
    GPIO.cleanup()


