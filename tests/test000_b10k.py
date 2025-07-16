# tests/test_b10k.py

import time
from labjack import ljm

# LabJack T7에 이더넷으로 연결
handle = ljm.openS("T7", "ETHERNET", "192.168.1.3")

try:
    print("B10K 전압 추출 시작 (1초에 10회)... 중지하려면 Ctrl+C")
    for _ in range(100):  # 총 10초 동안 수행
        voltage = ljm.eReadName(handle, "AIN0")
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] AIN0 전압: {voltage:.3f} V")
        time.sleep(0.1)  # 0.1초 간격 = 초당 10회
except KeyboardInterrupt:
    print("중단됨.")
finally:
    ljm.close(handle)
    print("LabJack 연결 종료")
