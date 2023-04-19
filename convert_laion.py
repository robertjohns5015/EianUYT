import json
import csv

# specify input and output file paths
input_file = 'laion_synthetic_filtered_large.json'


# extract header and data from JSON
header = data[0].keys()
rows = [x.values() for x in data]

# write data to TSV file
with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(header)
    writer.writerows(rows)
