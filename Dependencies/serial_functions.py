import serial.tools.list_ports

def get_com_ports():
    ports = serial.tools.list_ports.comports()
    devices=[]
    for port, desc, hwid in sorted(ports):
        devices.append(port)
    return devices