GOOGLE_DATA_SOURCES = [
{
  "name": "Microlife BP",
  "dataSourceId": "raw:com.google.heart_rate.bpm:get-fit:Microlife:B3:100001",
  "dataType": {
    "field": [
      {
        "name": "bpm",
        "format": "floatPoint"
      }
    ],
    "name": "com.google.heart_rate.bpm"
  },
  "application": {
    "name": "get-fit",
    "version": "1.0"
  },
  
  "device": {
    "model": "B3",
    "version": "1.0",
    "type": "watch",
    "uid": "100001",
    "manufacturer": "Microlife"
  },
  "type": "raw"
},

{
  "name": "Microlife BP 2",
  "dataSourceId": "raw:com.google.blood_pressure:get-fit:Microlife:B3:100002",
  "dataType": {
    "name": "com.google.blood_pressure"
   },
  "application": {
    "name": "get-fit",
    "version": "1.0"
  },
  "device": {
    "model": "B3",
    "version": "1.0",
    "type": "watch",
    "uid": "100001",
    "manufacturer": "Microlife"
  },
  "type": "raw"
}

]

