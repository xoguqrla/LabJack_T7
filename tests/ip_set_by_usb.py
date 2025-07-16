from labjack import ljm

# LabJack T7 USB 연결
handle = ljm.openS("T7", "USB", "ANY")
print("LabJack T7에 USB 연결됨")

# 새 IP 설정 정보
new_ip = "192.168.1.5"
new_subnet = "255.255.255.0"
new_gateway = "192.168.1.1"

# 문자열 IP → 32bit 정수 변환 함수
def ip_to_long(ip_str):
    octets = list(map(int, ip_str.strip().split('.')))
    return (octets[0]<<24) + (octets[1]<<16) + (octets[2]<<8) + octets[3]

# 변환
ip_long = ip_to_long(new_ip)
subnet_long = ip_to_long(new_subnet)
gateway_long = ip_to_long(new_gateway)

# LabJack T7에 IP 관련 설정 쓰기
ljm.eWriteName(handle, "ETHERNET_IP", ip_long)
ljm.eWriteName(handle, "ETHERNET_SUBNET", subnet_long)
ljm.eWriteName(handle, "ETHERNET_GATEWAY", gateway_long)

# Static IP 설정 (1: static, 0: DHCP)
ljm.eWriteName(handle, "ETHERNET_CONFIG_CURRENT", 1)  # 현재 설정 적용
ljm.eWriteName(handle, "ETHERNET_CONFIG_DEFAULT", 1)  # 재부팅 시 유지

print(f"IP 설정 완료: {new_ip}")
ljm.close(handle)
