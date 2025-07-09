import requests
import json
import gzip
import os
import config as cg
import pandas as pd
# import logWriter as lw
# import cleartax as ct
# import sqlServer as db
import logging
from logging.handlers import RotatingFileHandler
import time
from datetime import datetime
import numpy as np
import config as cg


# invoice_data = {}

# Function to create a logger with multiple file handlers
def setup_logger(name, log_file, level=logging.INFO):
    """Create a logger with the given name, log file, and log level."""
    
    log_dir = os.path.dirname('data/log_file')
    if not os.path.exists(log_dir) and log_dir != '':
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(level)

        # Create file handler for logging
        handler = RotatingFileHandler(log_file, maxBytes=2000000, backupCount=3)
        handler.setLevel(level)

        # Create a logging format that includes function name and line number
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - Line: %(lineno)d - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(handler)

    return logger

current_date = datetime.now().strftime("%Y-%m-%d")
info_filename = f'data/log_file/info_{current_date}.log'
error_filename = f'data/log_file/error_{current_date}.log'
# Create different loggers for different log files
info_logger = setup_logger('info_logger', info_filename, level=logging.INFO)
error_logger = setup_logger('error_logger', error_filename, level=logging.ERROR)

def header(gstin):
    headers = {
        "X-Cleartax-Auth-Token": cg.headToken,#"1.6fa08b96-6335-4b61-8159-7dee044061bd_4ca6350826c4053153ad317f0b3ab17b71f4d7ffa9088d4be595f206b43191a2",
        "gstin": str(gstin),
        "Content-Type": "application/json"
        # "Accept": "*/*"
    }
    return headers

def header_buyer():
    headers = {
        "x-cleartax-auth-token": cg.headToken_gst,#"1.6fa08b96-6335-4b61-8159-7dee044061bd_4ca6350826c4053153ad317f0b3ab17b71f4d7ffa9088d4be595f206b43191a2",
        "Content-Type": "application/json",
        "x-ct-api-key": cg.api_key,
        "x-ct-sourcetype": 'API',
        "Accept": "*/*"
    }
    return headers

def generate_IRN(json_file):
    try:
        invoice=[]
        invoice.append(json_file) 
        print(cg.api_url)
        print(invoice)
        response = requests.put(cg.api_url, headers=header(json_file['transaction']['SellerDtls']['Gstin']), json=invoice)

        response_data = response.json() #json.loads(response.text)

        print(response_data)
        info_logger.info(response_data)
        time.sleep(5)
    except Exception as e: 
            error_logger.error(f"Error while generating the IRN:{str(e)}")
    try:
        if response_data[0]["govt_response"]["ErrorDetails"][0]["error_code"] is not None:
            error_logger.error(f"Error genarting IRN: {str(error_message_list(response_data))}")
            return "", response_data
    except Exception as e:
        print(str(e))
        try:
            # print(response_data[0]["document_status"])
            if response_data[0]["document_status"] == "IRN_GENERATED":
                try:
                    irn = response_data[0]["govt_response"]["Irn"]
                    return irn, response_data
                    # pdf(irn, invoice_number, seller_gst, buyer_gst)
                except:

                    error_logger.error(f"Error genarting IRN: {str(error_message_list(response_data))}")
                    return "", response_data
            else:
                error_logger.error(f"Error genarting IRN: {str(error_message_list(response_data))}")
                return "", response_data
                # break
        except:

            error_logger.error(f"Error genarting IRN: {str(error_message_list(response_data))}")
            return "", response_data
        
def error_message_list(data):
    error_messages = []
    # Extract error messages from the provided data
    for entry in data:
        try:
            govt_response = entry["govt_response"]
            error_details = govt_response["ErrorDetails"]

            for error_detail in error_details:
                error_message = error_detail["error_message"]
                if error_message:
                    error_messages.append(error_message)
        except:
            try:
                error_messages = data["error_message"]
            except (KeyError, TypeError) as e:
                print("Error extracting messages:", e)

    return error_messages

def get_buyer(gstin):
    i = 1
    while(i==1):
        try:
            header = header_buyer()
            info_logger.info(f"The header for Buyer GSTIN API is {header}.")
            api_url = str(cg.get_buyer) + str(gstin)
            info_logger.info(f"The url for Buyer GSTIN API is {api_url}.")
            response = requests.get(api_url, headers=header)

            response_data = response.json() #json.loads(response.text)
            
            info_logger.info(f"The response for the Buyer GSTIN API is {response_data}.")
            print(response.status_code)
            if response.status_code == 200:
                try:
                    if (response['success'] == False) and (response['message'] == 'Invalid response returned by GSTN'):
                        pass
                    else:
                        return response_data
                except:
                    return response_data
            else:
                return response_data
            # time.sleep(10)

            # time.sleep(5)
        except Exception as e: 
            error_logger.error(f"Error while calling the Buyer GSTIN API:{str(e)}")
            i = i + 1


def pdf(irn):
    try:
        headers = header("27AAFCD5862R013") # 
        info_logger.info(f"The header for PDF is: {headers}")
        api_url = '{}format=PDF&irns={}&template=3956e98e-32d1-4df4-b5e9-39c716327c9y'.format(cg.api_pdf, irn)
        info_logger.info(f"The API url for PDF is: {api_url}")
        response_pdf = requests.get(
                api_url,
                headers=headers)
        info_logger.info(f"The json file for PDF is :{response_pdf}")
        return response_pdf
    except Exception as e: 
        error_logger.error(f"Error for PDF API is:{str(e)}")