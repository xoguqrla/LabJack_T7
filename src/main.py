import os
import time
import yaml
import logging
from ljm_interface import LabJackT7
from data_logger import save_data

# 로그 경로 및 파일 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(script_dir, "../logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "run.log")

logging.basicConfig(
    filename=log_file, filemode='a', encoding='utf-8', level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

config_path = os.path.join(script_dir, "../config/settings.yaml")
with open(config_path, encoding='utf-8') as f:
    config = yaml.safe_load(f)

ip = config['labjack']['ip_address']
channels = config['labjack']['channels']
interval = config['labjack']['sample_interval']
save_dir = os.path.join(script_dir, "..", config['data']['save_dir'].strip("/\\"))
file_prefix = config['data']['file_prefix']

lj = LabJackT7(ip)
data = []

logging.info(f"측정 시작: LabJack {ip}, 채널 {channels}, 간격 {interval}s")
try:
    for _ in range(10):
        voltages = lj.read_channels(channels)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data.append([timestamp] + list(voltages))
        print(dict(zip(channels, voltages)))
        logging.info(f"{timestamp} 측정값: {dict(zip(channels, voltages))}")
        time.sleep(interval)
except Exception as e:
    logging.error(f"측정 중 에러: {e}")
finally:
    lj.close()
    save_data(save_dir, file_prefix, channels, data)
    logging.info("측정 데이터 저장 완료, LabJack 연결 종료")

print(f"로그 파일이 {log_file}에 저장됩니다.")
