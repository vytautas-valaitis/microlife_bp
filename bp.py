import hid, ctypes

VENDOR = 0x04D9
PRODUCT = 0xB554

device = hid.Device(VENDOR, PRODUCT)

def checksum(data):
  cksum = sum(data[0:len(data) - 1]) % 256
  if(cksum == data[-1]):
    return True
  return False

def write(device, data):
  raw = ctypes.create_string_buffer(len(data) + 1)
  raw[0] = len(data)
  raw[1:] = data

  device.write(raw)

  data = bytearray()
  BUFFER_SIZE = 8
  TIMEOUT = 100

  while True:
    buf = device.read(BUFFER_SIZE, TIMEOUT)
    if not buf:
      break
    data.extend(buf[1:(buf[0] & 15) + 1])

  assert checksum(data)
  return data

def print_bp(data):
  cnt = 0
  first = 0
  for b in data:
    cnt += 1
    print('%d' % b, end = ' ')
    if(first == 0 and cnt == 42):
      print()
      first = 1
      cnt = 0
    if (first == 1 and cnt == 10):
      print()
      cnt = 0
  print()

if __name__ == '__main__':
  data = [0x4d, 0xff, 0x00, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfd, 0x52]
  assert checksum(data)
  data = write(device, data)
  print_bp(data)
