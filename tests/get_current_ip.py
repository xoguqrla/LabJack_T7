from labjack import ljm

def long_to_ip(val):
    return ".".join(str((val >> (8 * i)) & 0xFF) for i in reversed(range(4)))

try:
    handle = ljm.openS("T7", "USB", "ANY")  # USB로 T7에 연결
    print("LabJack T7에 USB 연결됨")

    # 현재 설정 값 읽기
    ip = int(ljm.eReadName(handle, "ETHERNET_IP"))
    subnet = int(ljm.eReadName(handle, "ETHERNET_SUBNET"))
    gateway = int(ljm.eReadName(handle, "ETHERNET_GATEWAY"))
    mode = int(ljm.eReadName(handle, "ETHERNET_DHCP_ENABLE"))  # 1이면 DHCP, 0이면 Static

    print("\n현재 LabJack T7 네트워크 설정:")
    print(f"  IP 주소       : {long_to_ip(ip)}")
    print(f"  서브넷 마스크 : {long_to_ip(subnet)}")
    print(f"  게이트웨이     : {long_to_ip(gateway)}")
    print(f"  IP 설정 방식   : {'DHCP' if mode else 'Static'}")

except Exception as e:
    print("오류 발생:", e)
finally:
    try:
        ljm.close(handle)
        print("LabJack 연결 종료")
    except:
        pass
