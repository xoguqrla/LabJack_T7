# tests/test001_b10k.py

import time
from labjack import ljm

# LabJack T7에 이더넷으로 연결
handle = ljm.openS("T7", "ETHERNET", "192.168.1.3")

# 사용할 디지털 출력 핀 설정 (예: FIO0 = DIO0)
dio_channel = "FIO0"
threshold = 3.0  # 임계값 (단위: Volt)

try:
    print("B10K 전압 추출 + 디지털 이진화 시작 (1초에 10회)... 중지하려면 Ctrl+C")
    for _ in range(200):  # 총 10초 수행
        voltage = ljm.eReadName(handle, "AIN0")
        digital_output = 1 if voltage >= threshold else 0

        # DIO 핀에 디지털 값 출력
        ljm.eWriteName(handle, dio_channel, digital_output)

        # 출력 로그
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] AIN0 전압: {voltage:.3f} V → {dio_channel} 출력: {digital_output}")

        time.sleep(0.25)  # 0.1초 간격
except KeyboardInterrupt:
    print("중단됨.")
finally:
    # 디지털 핀 0으로 리셋 후 종료
    ljm.eWriteName(handle, dio_channel, 0)
    ljm.close(handle)
    print("LabJack 연결 종료 및 DIO 핀 초기화 완료")
