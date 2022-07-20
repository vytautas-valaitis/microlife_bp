import hid, ctypes, datetime, pickle

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

ct = 0

def print_bp(data):
  for i in range(42):
    a = data.pop(0)  
    if(i == 0):
      assert a == 77
    if(i == 1):
      assert a == 58
    if(i == 7):
      ct = a

  record = [0, 0, 0, 0, 0]
  result = []
  cnt = 0
  date_y = 0
  date_m = 0
  date_d = 0
  date_hh = 0
  date_mm = 0
  
  for b in data:
    match cnt:
      case 0:
        record[1] = b # systolic
      case 1:
        record[2] = b # diastolic
      case 2:
        record[3] = b # pulse
      case 3:
        date_y = b
      case 4:
        date_m = b
      case 5:
        date_d = b
      case 6:
        date_hh = b
      case 7:
        date_mm = b
      case 8:
        record[4] = b # cuff wrongly placed, irregular rythm
      case 9:
        assert b == 0
        record[0] = datetime.datetime(2000 + date_y, date_m, date_d, date_hh, date_mm)
        result.append(record.copy())
        cnt = -1
    cnt += 1
  
  assert ct == len(result)
  
  for r in result:
    print(r)
    
  with open("data.pickle", "wb") as f:
    pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)
  
if __name__ == '__main__':
  data = [0x4d, 0xff, 0x00, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfd, 0x52]
  assert checksum(data)
  data = write(device, data)
  print_bp(data)
