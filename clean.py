import argparse
import csv
import re
import sys

# Increase max CSV field size
maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

parser = argparse.ArgumentParser(description="Clean HTML tags from CSV file.")
parser.add_argument("filename", help="CSV file to clean.")
parser.add_argument("-o", "--output", required=True, help="Output csv file.")

args = parser.parse_args()

def remove_html_tags_and_content(text):
    # Remove content within the <b class='tablesaw-cell-label'>...</b> tags
    text = re.sub(r"<b class='tablesaw-cell-label'>.*?</b>", '', text)

    # Remove any remaining HTML tags
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

with open(args.filename, "r") as input_file, open(args.output, "w") as output_file:
    for line in input_file:
        cleaned_line = remove_html_tags_and_content(line)
        output_file.write(cleaned_line)
