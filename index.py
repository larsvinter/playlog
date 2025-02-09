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
                        "path": "/mnt/s3bucket/uploads/ea1dd559-bb02-4abe-ac43-db7253f52019.wav",
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
                },
                {
                    "uuid": "jkljaksf834jh2",
                    "time": start_epoch_ms + 69031,
                    "type": "file",
                    "data": {
                        "path": "data/audio/Bed 1 - The Pirate.aif",
                        "sideChainType": "receive",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 85.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 15.407, "val": 1 },
                            { "pos": 15.740, "val": 0 }
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh3",
                    "time": start_epoch_ms + 71156,
                    "type": "file",
                    "data": {
                        "path": "data/audio/speak-1.wav",
                        "sideChainType": "trigger",
                        "vol": 0.9,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 85.000,
                        "envelope": []
                    }
                },
                {
                    "uuid": "jkljaksf834jh4",
                    "time": start_epoch_ms + 84414,
                    "type": "file",
                    "data": {
                        "path": "data/audio/Excellent.wav",
                        "sideChainType": "trigger",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 20.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 20.0, "val": 1 },
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh5",
                    "time": start_epoch_ms + 84757,
                    "type": "file",
                    "data": {
                        "path": "/mnt/s3bucket/uploads/6ccd7961-4491-44fa-b05a-bce434672b41.wav",
                        "sideChainType": "receive",
                        "vol": 0.8,
                        "speed": 1.0,
                        "begin": 2.2,
                        "end": 155.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 150.0, "val": 1 },
                            { "pos": 153.0, "val": 0 },
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh6",
                    "time": start_epoch_ms + 85146,
                    "type": "file",
                    "data": {
                        "path": "data/audio/speak-2.wav",
                        "sideChainType": "trigger",
                        "vol": 0.9,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 120.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 120.0, "val": 1 },
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh7",
                    "time": start_epoch_ms + 90989,
                    "type": "file",
                    "data": {
                        "path": "data/audio/speak-3.wav",
                        "sideChainType": "trigger",
                        "vol": 0.9,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 120.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 120.0, "val": 1 },
                        ]
                    }
                },
                {
                    "uuid": "jkljaksf834jh8",
                    "time": start_epoch_ms + 92377,
                    "type": "file",
                    "data": {
                        "path": "data/audio/one-great.wav",
                        "sideChainType": "receive",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.0,
                        "end": 120.000,
                        "envelope": [
                            { "pos": 0,      "val": 1 },
                            { "pos": 120.0, "val": 1 },
                        ]
                    }
                }
            ],
            "nextUpdate": start_epoch_ms + 1000 * 240
        }
    else:
        # Return empty for any other station_id
        return {}
