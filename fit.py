from get_googleaccount import main
from googleapiclient.errors import HttpError
from google_datasources import GOOGLE_DATA_SOURCES

service = main()

def CheckGoogleDataSourceExists(dataSourceId):
    try:
        service.users().dataSources().get(
            userId="me", dataSourceId=dataSourceId
        ).execute()
    except HttpError as error:
        if "DataSourceId not found" in str(error):
            return False
        else:
            raise error
    else:
        return True

def CreateGoogleDataSource(GoogleDataSourceJson):
    try:
        service.users().dataSources().create(
            userId="me", body=GoogleDataSourceJson
        ).execute()
    except HttpError as error:
        if "40" in str(error):
            raise error
    print("DataSource successfully created")
    
def UploadHrToGoogle(timeNs, hr):
    google_datapoint = {
        "minStartTimeNs":timeNs,
        "maxEndTimeNs":timeNs,
        "dataSourceId":"raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001",  #"raw:com.google.heart_rate.bpm:eb36738d:Microlife:B3:6f26fa75", #
        "point":[
              {"startTimeNanos": timeNs,
               "endTimeNanos": timeNs,
               "dataTypeName": "com.google.heart_rate.bpm",
               "value": [{"fpVal": hr}]
              }
        ]
    }
    
    datasetId = (
        str(google_datapoint["minStartTimeNs"])
        + "-"
        + str(google_datapoint["maxEndTimeNs"])
    )
    
    try:
        service.users().dataSources().datasets().patch(
            userId="me",
            dataSourceId="raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001",
            datasetId=datasetId,
            body=google_datapoint
        ).execute()
    except HttpError as error:
        raise error
    print("Uploaded HR data successfully")

def UploadBpToGoogle(timeNs, bp_sys, bp_dia):

    google_datapoint = {
    "minStartTimeNs": timeNs,
    "maxEndTimeNs": timeNs,
    "dataSourceId": "raw:com.google.blood_pressure:478274208348:Microlife:B3:100001",
    "point": [
      {
        "dataTypeName": "com.google.blood_pressure", 
        "startTimeNanos": timeNs,
        "endTimeNanos": timeNs,
        "value": [{"fpVal": bp_sys}, {"fpVal": bp_dia}, {}, {}]
      }
    ]
    }

    datasetId = (
        str(google_datapoint["minStartTimeNs"])
        + "-"
        + str(google_datapoint["maxEndTimeNs"])
    )
    
    try:
        service.users().dataSources().datasets().patch(
            userId="me",
            dataSourceId="raw:com.google.blood_pressure:478274208348:Microlife:B3:100001",
            datasetId=datasetId,
            body=google_datapoint
        ).execute()
    except HttpError as error:
        raise error
    print("Uploaded BP data successfully")    

def UploadBpHrList(data):
    for d in data:
        print(d)
        UploadHrToGoogle(d[0], d[3])
        UploadBpToGoogle(d[0], d[1], d[2])

if __name__=='__main__':
    #for x in GOOGLE_DATA_SOURCES:
    #    if not CheckGoogleDataSourceExists("raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001"):
    #        y = x.pop("dataSourceId")
    #        CreateGoogleDataSource(x)

    #UploadHrToGoogle()
    #UploadBpToGoogle()
    pass

