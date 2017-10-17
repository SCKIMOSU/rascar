# 교과목명: 창업연계공학설계입문
# 일자: 2017 년 9월 28 일
# 내 용: 초음파 센서의 거리데이터를 입력받아, 거리계산 후 터미널에 출력하기


import RPi.GPIO as GPIO
import time
from time import sleep

def ultra():

    GPIO.setmode(GPIO.BOARD)  # Board Mode and BCM Mode

    trig=33  # 초음파 센서의 trig핀(음파송신)은 Raspberry Pi의 GPIO 33번 핀과 연결됨
    echo=31  # 초음파 센서의 echo핀(음파수신)은 Raspberry Pi의 GPIO 31번 핀과 연결됨

    #ultrasonic sensor setting
    GPIO.setup(trig,GPIO.OUT) # Raspberry Pi의 GPIO 33핀을 OUT핀으로 설정하여 음파가 송신되도록하는 명령어를 Raspberry Pi에서 초음파센서에게 보낸다(out설정이유, trig)
    GPIO.setup(echo,GPIO.IN) # Raspberry Pi의 GPIO 31핀을 IN핀으로 설정하여 음파가 수신되도록한다.

    try:
        while True:
            GPIO.output(trig,False) #초음파센서 trig에 False신호를 0.5초간 주어 초음파센서를 초기화한다
            time.sleep(0.5)
            GPIO.output(trig,True) #초음파센서 trig에 True신호를 0.00001초간 주어 초음파센서에서 초음파가 발사되도록 한다
            time.sleep(0.00001)
            GPIO.output(trig,False)  #초음파센서 trig에 False신호를 주어 초음파 발사를 마친다.
            while GPIO.input(echo)==0:  #
                pulse_start=time.time() # trig가 끝난 바로 직후에는 반사(echo)되어오는 초음파 신호가 아직 도달하지 않았다.
                # 즉, trig를 금방 끝마친 상황이다. pulse_start, 이때부터 반사되어 echo가 올 때까지 시간을 계산해야한다.
            while GPIO.input(echo)==1: # 반사되어 echo 신호가 도달한다. (pulse_end)
                pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start # 왕복되어 온 시간은 pulse_end- pulse_start
            distance=pulse_duration*17000 # 속도=거리/시간에서 거리는 속도*시간이다.
            # 음속: 340m/1초, 34000cm/1초, (1m=100cm), 340000*pulse_duration/2 = 17000*pulse_duration
            # 왕복거리가 아니라 편도거리임로 왕복되어 온 시간을 나누기 2를 한다 (pulse_end- pulse_start)/2 :
            distance=round(distance,2)
            print(distance)
      
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    ultra()
