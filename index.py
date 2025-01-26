import json
import time
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Print the entire event object for debugging
    print("Event: ", event)
    
    try:
        # Extract the stationId from the path parameters (as a string)
        station_id = event['pathParameters']['stationId']
        
        # Fetch the playlog for the given stationId (now as a string)
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
            "body": json.dumps({"error": "Bad Request", "message": f"Missing parameter: {str(e)}"})
        }
    
    return response

# Dummy function to simulate fetching playlog
def get_playlog_for_station(station_id):
    """
    station_id is now a string. We compare it to "KQLZ".
    If you need to handle multiple string station IDs, you can expand this logic.
    """
    now = datetime.now()
    
    # Compare as a string
    if station_id == "KQLZ":
        # Calculate the start and stop times 
        start_time = now + timedelta(seconds=10)
        start_epoch_ms = int(start_time.timestamp() * 1000)
        
        return  { 
            "items": [
                {
                    "uuid": "jkljaksf834jhk",
                    "time": start_epoch_ms,
                    "type": "file",
                    "data": {
                        "path": "data/audio/news.wav",
                        "sideChainType": "receive",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 61.000,
                        "envelope": [
                            { "pos": 0,      "val": 0 },
                            { "pos": 0.1,    "val": 1 },
                            { "pos": 60.875, "val": 1 },
                            { "pos": 61.000, "val": 0 }
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh1",
                    "time": start_epoch_ms + 60 * 1000,
                    "type": "file",
                    "data": {
                        "path": "data/audio/friday-opener.wav",
                        "sideChainType": "receive",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 17.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 16.0, "val": 1 },
                            { "pos": 17.0, "val": 0 }
                        ]
                    }
                }
            ],
            "nextUpdate": start_epoch_ms + 1000 * 240
        }
    else:
        # Return empty for any other station_id
        return {}
