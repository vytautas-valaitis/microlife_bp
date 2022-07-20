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

def UploadIfitBpToGoogle():

    google_datapoint = {
    "minStartTimeNs": 1658249100000000000,
    "maxEndTimeNs": 1658249210000000000,
    "dataSourceId": "raw:com.google.blood_pressure:478274208348:Microlife:B3:100001",
    "point": [
      {
        "dataTypeName": "com.google.blood_pressure", 
        "startTimeNanos": 1658249100000000000,
        "endTimeNanos": 1658249110000000000,
        "value": [{"fpVal": 120.0}, {"fpVal": 80.0}, {}, {}]
      }
    ]
    }
    
    print(google_datapoint)
    
    '''
    a = service.users().dataSources().datasets().get(
        userId='me',
        dataSourceId="raw:com.google.blood_pressure:478274208348:Microlife:B3:100001",
        datasetId="1658249110000000000-1658249100011111111",
    ).execute()
    print(a)
    '''
    try:
        service.users().dataSources().datasets().patch(
            userId="me",
            dataSourceId="raw:com.google.blood_pressure:478274208348:Microlife:B3:100001",
            datasetId="1658249110000000000-1658249110011111111",
            body=google_datapoint
        ).execute()
    except HttpError as error:
        raise error
    print("Uploaded BP data successfully")    
    
def CreateGoogleDataSource(GoogleDataSourceJson):
    try:
        service.users().dataSources().create(
            userId="me", body=GoogleDataSourceJson
        ).execute()
    except HttpError as error:
        if "40" in str(error):
            raise error
    print("DataSource successfully created")
    
def UploadIfitHrToGoogle():
    google_datapoint = {
        "minStartTimeNs":1658249100000000000,
        "maxEndTimeNs":1658249210000000000,
        "dataSourceId":"raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001",  #"raw:com.google.heart_rate.bpm:eb36738d:Microlife:B3:6f26fa75", #
        "point":[
              {"startTimeNanos": 1658249100000000000,
               "endTimeNanos": 1658249100000000000,
               "dataTypeName": "com.google.heart_rate.bpm",
               "value": [{"fpVal": 66.6}]
              }
        ]
    }
    print(google_datapoint)
    '''
    datasetId = (
        str(google_datapoint["minStartTimeNs"])
        + "-"
        + str(google_datapoint["maxEndTimeNs"])
    )
    '''
    try:
        service.users().dataSources().datasets().patch(
            userId="me",
            dataSourceId="raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001",
            datasetId="1658249110000000000-1658249100011111111", #datasetId,
            body=google_datapoint
        ).execute()
    except HttpError as error:
        raise error
    print("Uploaded HR data successfully")
    '''
    
if __name__=='__main__':
    #for x in GOOGLE_DATA_SOURCES:
    #    if not CheckGoogleDataSourceExists("raw:com.google.heart_rate.bpm:478274208348:Microlife:B3:100001"):
    #        y = x.pop("dataSourceId")
    #        CreateGoogleDataSource(x)

    #UploadIfitHrToGoogle()
    UploadIfitBpToGoogle()

