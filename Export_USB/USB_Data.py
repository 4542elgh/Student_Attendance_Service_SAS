import usb.core
import usb.util

dev = usb.core.find(find_all=True)

if dev is None:
    raise ValueError('Device not found')