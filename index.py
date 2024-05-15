import json
import time
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Print the entire event object for debugging
    print("Event: ", event)
    
    try:
        # Extract the stationId from the path parameters
        station_id = event['pathParameters']['stationId']
        
        # Convert station_id to integer for comparison
        station_id = int(station_id)
        
        # Fetch the playlog for the given stationId
        playlog = get_playlog_for_station(station_id)
        
        # Create a response object
        response = {
            "statusCode": 200,
            "body": json.dumps(playlog)
        }
    except KeyError as e:
        # Handle the case where the path parameter is missing
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Bad Request", "message": str(e)})
        }
    except ValueError as e:
        # Handle the case where the stationId is not an integer
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Bad Request", "message": "Invalid stationId"})
        }
    
    return response

# Dummy function to simulate fetching playlog
def get_playlog_for_station(station_id):
    now = datetime.now()
    
    if station_id == 101:
        # Calculate the start and stop times for station 101
        start_time = now + timedelta(minutes=1)
        stop_time = now + timedelta(minutes=2)
        
        # Convert datetime to epoch milliseconds
        start_epoch_ms = int(start_time.timestamp() * 1000)
        stop_epoch_ms = int(stop_time.timestamp() * 1000)

        # Replace this with your actual logic to fetch the playlog
        return  [
                    {
                        "seqNo": 1000,
                        "file": "aiff",
                        "start": start_epoch_ms,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": True,
                        "canBeDucked": True,
                        "speed": 1.0,
                        "gain": 0.9
                    }
                ]
    elif station_id == 102:
        # Calculate the start and stop times for station 102
        start_time = now + timedelta(minutes=1)
        stop_time = now + timedelta(minutes=2)
        
        # Convert datetime to epoch milliseconds
        start_epoch_ms = int(start_time.timestamp() * 1000)
        stop_epoch_ms = int(stop_time.timestamp() * 1000)

        # Replace this with your actual logic to fetch the playlog
        return  [
                    {
                        "seqNo": 2000,
                        "file": "wave",
                        "start": start_epoch_ms,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": True,
                        "canBeDucked": True,
                        "speed": 1.8,
                        "gain": 0.9
                    }
                ]
    else:
        # Return an empty array for any other station_id
        return []

