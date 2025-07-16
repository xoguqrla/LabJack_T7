from labjack import ljm

# USB로 T7 연결
handle = ljm.openS("T7", "USB", "ANY")
print("LabJack T7에 USB 연결됨")

def ip_from_long(ip_long):
    return ".".join([str((ip_long >> (8 * i)) & 0xFF) for i in reversed(range(4))])

try:
    ip_long = int(ljm.eReadName(handle, "ETHERNET_IP"))
    subnet_long = int(ljm.eReadName(handle, "ETHERNET_SUBNET"))
    gateway_long = int(ljm.eReadName(handle, "ETHERNET_GATEWAY"))
    dhcp_enabled = int(ljm.eReadName(handle, "ETHERNET_DHCP_ENABLE"))

    print("\n현재 LabJack T7 네트워크 설정:")
    print(f"  IP 주소       : {ip_from_long(ip_long)}")
    print(f"  서브넷 마스크 : {ip_from_long(subnet_long)}")
    print(f"  게이트웨이     : {ip_from_long(gateway_long)}")
    print(f"  IP 설정 방식   : {'DHCP' if dhcp_enabled else 'Static'}")

finally:
    ljm.close(handle)
    print("LabJack 연결 종료")
