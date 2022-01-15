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

### Logging:
To monitor which data-files are created (and where) a logging file is created in the same directory as the script. 
New logs are appended to a logging file, if the logging file already exists.

## Example data:

original:     
```
Specimen properties : Anvil height,"3,11",mm
Specimen properties : Geometry,Circular
Specimen properties : Area,"100,0",mm^2
Specimen properties : Final anvil height,"2,22",mm
Specimen properties : Final area,"100,1",mm^2
Specimen properties : Specimen label,""
Specimen properties : Diameter,"14,0",mm
Specimen properties : Final diameter,"14,0",mm

Time,Extension,Load,Compressive strain (Extension),Compressive stress,Cycle count
(s),(mm),(N),(mm/mm),(MPa),
"0,0","0,0","0,0","0,0","0,0","0,0"
"0,1","-0,02","-0,02","-0,01","0,0","0,0"
```

re-formatted:     
```
Specimen properties : Anvil height;3,11;mm
Specimen properties : Geometry;Circular
Specimen properties : Area;100.0;mm^2
Specimen properties : Final anvil height;2.22;mm
Specimen properties : Final area;100.1;mm^2
Specimen properties : Specimen label;
Specimen properties : Diameter;14.0;mm
Specimen properties : Final diameter;14.0;mm

Time;Extension;Load;Compressive strain (Extension);Compressive stress;Cycle count
(s);(mm);(N);(mm/mm);(MPa);
0.0;0.0;0.0;0.0;0.0;0.0
0.1;-0.02;-0.02;-0.01;0.0;0.0
```
