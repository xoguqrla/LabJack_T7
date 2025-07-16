import time
from labjack import ljm

# 설정값
DEVICE_TYPE = "T7"
CONNECTION_TYPE = "ETHERNET"
IP_ADDRESS = "192.168.1.5"
AIN_CHANNEL = "AIN0"
DIO_CHANNEL = "FIO0"
THRESHOLD = 3.0  # 전압 임계값
INTERVAL = 0.25  # 측정 간격 (초)

# LabJack T7에 연결
handle = ljm.openS(DEVICE_TYPE, CONNECTION_TYPE, IP_ADDRESS)

try:
    print(f"LabJack T7({IP_ADDRESS}) 연결됨 - 아날로그 입력 측정 및 디지털 출력 시작")
    while True:
        # 아날로그 전압 읽기
        voltage = ljm.eReadName(handle, AIN_CHANNEL)

        # 디지털 이진화: THRESHOLD 기준
        digital_output = 1 if voltage >= THRESHOLD else 0
        ljm.eWriteName(handle, DIO_CHANNEL, digital_output)

        # 출력
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {AIN_CHANNEL} 전압: {voltage:.3f} V → {DIO_CHANNEL} 출력: {digital_output}")

        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("\n사용자 중단 (Ctrl+C)")
finally:
    # 디지털 핀 초기화 후 연결 종료
    ljm.eWriteName(handle, DIO_CHANNEL, 0)
    ljm.close(handle)
    print("LabJack 연결 종료 및 디지털 핀 초기화 완료")
