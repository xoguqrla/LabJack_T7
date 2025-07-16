# 디지털 입력 신호 읽기 및 처리
# 디지털 신호 출력 검증 코드임
# tests/test002.py

import time
from labjack import ljm

# LabJack 연결
handle = ljm.openS("T7", "ETHERNET", "192.168.1.3")

# DIO 핀 정의
dio_output = "FIO0"  # 디지털 출력 (from B10K 분석)
dio_input = "FIO1"   # 디지털 입력 (FIO0과 연결된 핀)

try:
    print("FIO1 디지털 입력 감지 시작 (1초에 10회)... 중지하려면 Ctrl+C")
    for _ in range(500):
        # 디지털 입력 상태 읽기
        digital_input = ljm.eReadName(handle, dio_input)

        # 이진값 처리 (보통 0.0 또는 1.0으로 읽힘)
        state = int(digital_input)

        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {dio_input} 입력 감지: {state}")

        # 신호 처리 예: 조건에 따른 메시지 출력
        if state == 1:
            print("  → 기준 전압 이상 (활성화 상태 감지)")
        else:
            print("  → 기준 전압 이하 (비활성 상태)")

        time.sleep(0.25)
except KeyboardInterrupt:
    print("중단됨.")
finally:
    ljm.close(handle)
    print("LabJack 연결 종료")
