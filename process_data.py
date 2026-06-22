import json
import os

print("Extracting raw data...")
raw_data = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Mark", "status": "INACTIVE"},
    {"id": 3, "name": "Charlie", "status": "Active"}
]
print("Transforming data...")
cleaned_data = []
for record in raw_data:
    record['status'] = record['status'].lower()
    cleaned_data.append(record)
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

with open(f"{output_dir}/clean_data.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)

print(f"Success! Processed {len(cleaned_data)} records and saved to {output_dir}/clean_data.json")