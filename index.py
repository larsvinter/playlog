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
                    "uuid": "jkljashf834jh5",
                    "time": start_epoch_ms,
                    "type": "file",
                    "category": "music",
                    "data": {
                        "artist": "Rihanna",
                        "title": "Diamonds",
                        "path": "/audio/rihanna.wav",
                        "waveformPath": "/audio/rihanna.dat",
                        "coverArtPath": "/audio/rihanna.jpg",
                        "sideChainType": "receive",
                        "audioType": "main",
                        "vol": 0.97,
                        "speed": 1.0,
                        "begin": 0.000,
                        "end": 3 * 60 + 43,
                        "envelope": [
                            { "pos": 0,      "val": 0 },
                            { "pos": 0,      "val": 1 },
                            { "pos": 3 * 60 + 41, "val": 1 },
                            { "pos": 3 * 60 + 43, "val": 0 }
                        ]
                    }
                },
                {
                    "uuid": "jkljashf834jh6",
                    "time": start_epoch_ms + 218993,
                    "type": "file",
                    "category": "speak",
                    "data": {
                        "host": "Rachal Morgan",
                        "text": "That was Rihanna with Diamonds — did you know the song was actually written in just 14 minutes by Sia? Talk about a hit in record time! And now, switching gears to a 90s classic—Wilson Phillips with: Hold On...",
                        "path": "/audio/pvc_s54_sb79_se37_m2.wav",
                        "waveformPath": "/audio/pvc_s54_sb79_se37_m2.dat",
                        "coverArtPath": "/audio/rachel.jpg",
                        "sideChainType": "trigger",
                        "audioType": "overlay",
                        "vol": 1.2,
                        "speed": 1.0,
                        "begin": 0.000,
                        "end": 15,
                        "envelope": []
                    }
                },
                {
                    "uuid": "jkljashf834jh7",
                    "time": start_epoch_ms + 219500,
                    "type": "file",
                    "category": "music",
                    "data": {
                        "artist": "Wilson Phillips",
                        "title": "Hold On",
                        "path": "/audio/wilson.wav",
                        "waveformPath": "/audio/wilson.dat",
                        "coverArtPath": "/audio/wilson.jpg",
                        "sideChainType": "receive",
                        "audioType": "main",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.000,
                        "end": 3 * 60 + 5,
                        "envelope": [
                            { "pos": 0,      "val": 0 },
                            { "pos": 0,      "val": 1 },
                            { "pos": 3 * 60, "val": 1 },
                            { "pos": 3 * 60 + 3, "val": 0 }
                        ]
                    }
                },
                {
                    "uuid": "jkljashf834jh7",
                    "time": start_epoch_ms + 319500,
                    "type": "file",
                    "category": "music",
                    "data": {
                        "artist": "Avicii",
                        "title": "Levels",
                        "path": "/mnt/s3bucket/items/avicii.wav",
                        "waveformPath": "/mnt/s3bucket/items/avicii.dat",
                        "coverArtPath": "/mnt/s3bucket/items/avicii.jpg",
                        "sideChainType": "receive",
                        "audioType": "main",
                        "vol": 1.0,
                        "speed": 1.0,
                        "begin": 0.000,
                        "end": 3 * 60 + 5,
                        "envelope": [
                            { "pos": 0,      "val": 0 },
                            { "pos": 0,      "val": 1 },
                            { "pos": 3 * 60, "val": 1 },
                            { "pos": 3 * 60 + 3, "val": 0 }
                        ]
                    }
                },
            ],
            "nextUpdate": start_epoch_ms + 1000 * 460
        }
    else:
        # Return empty for any other station_id
        return {}
