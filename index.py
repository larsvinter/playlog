import json

def lambda_handler(event, context):
    # Extract the stationId from the path parameters
    station_id = event['pathParameters']['stationId']
    
    # You can now use the stationId in your logic
    # For example, fetch the playlog for the given stationId
    playlog = get_playlog_for_station(station_id)
    
    # Create a response object
    response = {
        "statusCode": 200,
        "body": json.dumps(playlog)
    }
    
    return response

# Dummy function to simulate fetching playlog
def get_playlog_for_station(station_id):
    # Replace this with your actual logic to fetch the playlog
    return {
        "stationId": station_id,
        "playlog": [
            {"song": "Song 1", "artist": "Artist 1"},
            {"song": "Song 2", "artist": "Artist 2"}
        ]
    }