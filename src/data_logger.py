import csv
import os
from datetime import datetime

def save_data(save_dir, file_prefix, channels, data):
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{file_prefix}{datetime.now():%Y%m%d_%H%M%S}.csv"
    filepath = os.path.join(save_dir, filename)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp'] + channels)
        for row in data:
            writer.writerow(row)
    return filepath
