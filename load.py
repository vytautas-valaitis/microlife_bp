import pickle
from fit import UploadBpHrList

if __name__=='__main__':
  with open("data.pickle", "rb") as f:
    data = pickle.load(f)
    
    for d in data:
      bp_time = int(d[0].timestamp())*1000000000 # seconds to nanoseconds
      bp_sys = d[1]
      bp_dia = d[2]
      bp_pulse = d[3]
      
      print(d[0], end='')      
      print("  %d/%d %d" % (bp_sys, bp_dia, bp_pulse))
      d[0] = bp_time 
    
    UploadBpHrList(data)
      
