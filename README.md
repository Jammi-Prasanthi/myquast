# myquast
The myquast.py script is a Python script that calculates assembly metrics of a genome assembly in a FASTA file format. The script uses the Biopython library to parse the FASTA file and extract the necessary information to calculate the metrics. The metrics calculated are:

Number of contigs
Total length
Largest contig
N50

The script takes two arguments namely the path to the input FASTA file or the name of input file and the name of the output file or directory where the above mentioned metrics will be saved. If any output directory is not mentioned, then by default the result will be saved to the report.txt in the current working directory/folder.

Directions to use the script
To use the myquast.py script, follow these steps:

1. Copy the script and paste it into a new file named myquast.py.
2. Check if you have Biopython library installed in your Python environment. If not, you can install it using pip install biopython.
3. Run the script from the command line using the following command:
       python myquast.py input.fasta -o output_file.txt
    
    In the above command, input.fasta is the path to the file which has the contigs generated from genome assembly, whereas output_file.txt is the path to the output directory where you wanr your file to be saved. 
4. if the command does not work try the following 
  
       python path_Where_myquast.py_is_saved input.fasta -o output_file.txt
          
       Instead of myquast.py, give the path where the executable python file is saved

5. Note that if you have not specified any output directory path, don't worry! please check for a file named report.txt in your current working folder which will have the desired results.
            

