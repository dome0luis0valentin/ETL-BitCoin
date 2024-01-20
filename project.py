from extract import extract
from transform import transform
from load import load
from datetime import datetime

file_log = "log.txt"

def add_log(message):
        timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthcar_model-Day-Hour-Minute-Second 
        now = datetime.now() # get current timestamp 
        timestamp = now.strftime(timestamp_format) 
        with open(file_log,"a") as f: 
                f.write("\n##"+timestamp + ',' + message + '\n') 
                
add_log("Beging the process of ETL") 

add_log("Start extraction of data")  
price_dolar = extract()
if price_dolar is None:
    add_log("Erro in connection to API")
else:
    add_log("Extract ended")

    add_log("Start transformation of data")  
    df = transform(price_dolar)
    add_log("Transformation ended")

    add_log("Start loading of data")  
    load()
    add_log("Load ended")

