import getmac
import psutil

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow


print("Running main")
deviceMac = getmac.get_mac_address()

print(f"Device MAC address is: {deviceMac}")

# gives a single float value
print(psutil.cpu_percent())
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary
print(dict(psutil.virtual_memory()._asdict()))
# you can have the percentage of used RAM
print(psutil.virtual_memory().percent)

# you can calculate percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

