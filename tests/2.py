from labjack import ljm

def ip_to_long(ip_str):
    octets = list(map(int, ip_str.strip().split('.')))
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def set_labjack_static_ip(ip, subnet, gateway):
    try:
        handle = ljm.openS("T7", "USB", "ANY")
        print("LabJack T7에 USB 연결됨")

        ip_long = ip_to_long(ip)
        subnet_long = ip_to_long(subnet)
        gateway_long = ip_to_long(gateway)

        # Static IP 구성 레지스터
        ljm.eWriteName(handle, "ETHERNET_IP_DEFAULT", ip_long)
        ljm.eWriteName(handle, "ETHERNET_SUBNET_DEFAULT", subnet_long)
        ljm.eWriteName(handle, "ETHERNET_GATEWAY_DEFAULT", gateway_long)
        ljm.eWriteName(handle, "ETHERNET_DHCP_ENABLE_DEFAULT", 0)  # Static IP 모드

        print(f"설정 완료: IP={ip}, Subnet={subnet}, Gateway={gateway} (Static)")
        print("→ 장치를 재시작하면 해당 설정이 적용됩니다.")
    except Exception as e:
        print("오류 발생:", e)
    finally:
        ljm.close(handle)
        print("LabJack 연결 종료")

def prompt_user_and_apply():
    print("LabJack T7 Static IP 설정")
    ip = input("새 IP 주소 입력 (예: 192.168.1.5): ").strip()
    subnet = input("서브넷 마스크 입력 (예: 255.255.255.0): ").strip()
    gateway = input("게이트웨이 주소 입력 (예: 192.168.1.1): ").strip()

    set_labjack_static_ip(ip, subnet, gateway)

if __name__ == "__main__":
    prompt_user_and_apply()