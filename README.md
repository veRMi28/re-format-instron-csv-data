# re-format measurement results (CSV files) from an Universal test machine Instrom 5967
re-format output CSV data by Universal test machine Instrom 5967 and save re-formated data as new file. 
The script is obviously also usable for re-formatting other data files ;-)

## What is re-formatted?
This script is used to convert the formatting of csv files

Formatting changes are:
* decimal separator from comma to point
* column separator from comma to semicolon
* remove parentheses around values

## Usage:

### Script placement:
place the script in the top directory where you have data for conversion. There can be subdirectories with further data, the scripts searches for those files recursively

### run:
`python convert_decimals.py`
then it converts only file with the name "Specimen_RawData_1.csv" (default regular expression built-in)

Or specify a regular expression, e.g. like:     
`python convert_decimals.py [a-zA-Z0-9_]+RawData_[0-9].csv`      
or     
`python convert_decimals.py Specimen_RawData_1.csv`     

Converted files receive a filename following the pattern `<old-filename>_decsep.csv`
