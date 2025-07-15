from labjack import ljm

class LabJackT7:
    def __init__(self, ip_address):
        self.handle = ljm.openS("T7", "ETHERNET", ip_address)

    def read_channels(self, channels):
        return ljm.eReadNames(self.handle, len(channels), channels)

    def close(self):
        ljm.close(self.handle)
