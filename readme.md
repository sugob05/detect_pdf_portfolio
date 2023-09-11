#PDF File Analyzer
The PDF File Analyzer is a Python command-line tool that allows you to analyze PDF files within a specified source directory. It identifies the type of each PDF file, such as whether it's a standard PDF or a portfolio PDF. The tool then generates a report and writes it to a target file.

##Features
Analyze PDF files in a source directory.
Identify standard PDFs and portfolio PDFs.
Generate a report with file types.
Write the report to a target file.

##Prerequisites
Before using this tool, ensure you have the following prerequisites:

Python 3.x installed on your system.
The required Python packages installed. You can install them using pip:
bash
Copy code
pip install PyMuPDF argparse
Usage
To use the PDF File Analyzer, follow these steps:

Open your terminal or command prompt.

Navigate to the directory containing the script.

Run the script with the following command:

bash


python pdf_file_analyzer.py [source_directory] [target_file]
[source_directory]: The source directory containing the PDF files you want to analyze.
[target_file]: The target file where the analysis report will be written.
If you don't provide source_directory and target_file as command-line arguments, the script will prompt you to enter them.

Example:

python pdf_file_analyzer.py /path/to/source_directory report.txt
The tool will start analyzing the PDF files in the source directory.

If the target file already exists, you'll be prompted to confirm whether you want to overwrite it.

The tool will generate a report, indicating whether each PDF file is a standard PDF, a portfolio PDF, or an encrypted PDF.

The report will be written to the specified target file.

##File Types
PDF: Standard PDF file.
PortfolioPDF: Portfolio PDF file.
Encrypted PDF: Encrypted PDF file.

##License
This tool is released under the MIT License.

