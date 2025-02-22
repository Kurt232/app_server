from pymongo import MongoClient
from datetime import datetime
import csv

root = "/root/ops"
# Connect to MongoDB (adjust the URI if needed)
client = MongoClient('mongodb://localhost:27017/')

# Select the 'app' database
db = client['app']

# List all collection names in the database
all_collections = db.list_collection_names()

# Filter collections that start with 'imu_'
imu_collections = [coll for coll in all_collections if coll.startswith("imu_")]

# Data rows for CSV
data_rows = []

# For each collection, aggregate documents by day using the 'timestamp' field
for coll in imu_collections:
    collection = db[coll]
    # Remove the "imu_" prefix for display purposes
    collection_name = coll.replace("imu_", "")
    
    pipeline = [
        # Ensure the document has a timestamp field
        { "$match": { "timestamp": { "$exists": True } } },
        # Group by day using $dateToString to format the date as YYYY-MM-DD
        { "$group": {
            "_id": { "$dateToString": { "format": "%Y-%m-%d", "date": "$timestamp" } },
            "count": { "$sum": 1 }
        } },
        # Sort by date
        { "$sort": { "_id": 1 } }
    ]
    
    results = list(collection.aggregate(pipeline))
    
    # Print collection header and counts by date
    for result in results:
        date_str = result['_id']
        count = result['count']
        data_rows.append([collection_name, date_str, count])

# Now, sort the final data_rows by Date (column index 1)
data_rows = sorted(data_rows, key=lambda row: row[1])

# Save the aggregated data to CSV file with a timestamp in its filename
timestamp = datetime.now().strftime("%m%dT%H%M")
csv_filename = f"{root}/imu_collections_by_day_{timestamp}.csv"

with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # CSV header
    writer.writerow(["Collection", "Date", "Document Count"])
    writer.writerows(data_rows)

print(f"Data saved to {csv_filename}")