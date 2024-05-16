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
        start_time = now + timedelta(seconds=10)
        stop_time = now + timedelta(minutes=1)
        
        # Convert datetime to epoch milliseconds
        start_epoch_ms = int(start_time.timestamp() * 1000)
        stop_epoch_ms = int(stop_time.timestamp() * 1000)

        # Replace this with your actual logic to fetch the playlog
        return  [
                    {
                        "seqNo": 1000,
                        "file": "(Song) The Power Station (Shout) Copenhagen FM.wav",
                        "start": start_epoch_ms,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": True,
                        "canBeDucked": True,
                        "speed": 1.0,
                        "gain": 0.9,
                        "cue": 0,
                        "volEnvelope": []
                    },
                    {
                        "seqNo": 1001,
                        "file": "16450838_Wounded feat. Cara Melín_(Kristian Nairn Extended Remix).aiff",
                        "start": start_epoch_ms + 5000,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": True,
                        "canBeDucked": True,
                        "speed": 1.0,
                        "gain": 0.9,
                        "cue": 0,
                        "volEnvelope": [
                            { "pos": 0, "value": 1.0 },
                            { "pos": 800, "value": 1.0 },
                            { "pos": 1000, "value": 0.2 },
                            { "pos": 6000, "value": 0.2 },
                            { "pos": 8500, "value": 1.0 },
                        ]
                    },
                    {
                        "seqNo": 1002,
                        "file": "mark-speak.aif",
                        "start": start_epoch_ms + 6000,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": False,
                        "canBeDucked": False,
                        "speed": 1.0,
                        "gain": 1.0,
                        "cue": 0,
                        "volEnvelope": []
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
                        "file": "17800302_Other Side of the World_(Extended Mix).aiff",
                        "start": start_epoch_ms,
                        "stop": stop_epoch_ms,
                        "isUnderlay": False,
                        "shouldDuckPrev": True,
                        "canBeDucked": True,
                        "speed": 1.8,
                        "gain": 0.9,
                        "cue": 100,
                        "volEnvelope": [
                            { "pos": 10, "value": 60.4 },
                            { "pos": 2000, "value": 70.2 }
                        ]
                    }
                ]
    else:
        # Return an empty array for any other station_id
        return []

