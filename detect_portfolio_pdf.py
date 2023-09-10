import argparse
import os
import fitz


def run_os_scandir(directory: str, dironly: bool = True, onlyfiletype: str = False):
    """
    Get all the directories or files in a directory as an array.

    Args:
    directory (str): The path to the directory.
    dironly (bool, optional): If set to True, only directories are returned. Defaults to True.
    onlyfiletype (Optional[str], optional): The file type to be returned. Defaults to False.

    Returns:
    List[str]: A list of the directories or files in the directory.

    """
    
    if dironly:
        files_or_dirs = [f.path for f in os.scandir(directory) if f.is_dir()]
    elif onlyfiletype:
        files_or_dirs = [f.path for f in os.scandir(directory) if os.path.splitext(f.path)[1] == onlyfiletype]
    else:
        files_or_dirs = [f.path for f in os.scandir(directory)]

    return files_or_dirs


def check_file_if_portfolio(file_path):

	try:
		pdf = fitz.open(file_path)
		if pdf.is_encrypted:
			return "Encrypted PDF"
		


		
		if pdf.embfile_count()>0:
			return("PortfolioPDF")
		else: return "PDF"
	except:
		pass

def main():
    parser = argparse.ArgumentParser(description="Analyse PDF-files from a source directory and write it to a target file.")
    parser.add_argument("source_directory", nargs="?", help="The source directory containing files to copy.")
    parser.add_argument("target_file", nargs="?", help="The target file where files will be copied.")
    args = parser.parse_args()

    source_directory = args.source_directory
    target_file = args.target_file

    #Check if source directory is given
    if not source_directory:
        source_directory = input("Enter the source directory: ")

    #Check if target file is given
    if not target_file:
        target_file = input("Enter the target file: ")

    #Check if source directory exists
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return

    #Check if source directory is a directory
    if not os.path.isdir(source_directory):
        print(f"Error: '{source_directory}' is not a directory.")
        return

    # Check if the target file already exists
    if os.path.exists(target_file):
        overwrite = input(f"Warning: Target file '{target_file}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation canceled.")
            return
            
    # Scan directory
    source_files_array=run_os_scandir(source_directory,dironly=False, onlyfiletype=".pdf")
    
    #Open targetfilehandle
    target_filehandle=open(target_file, "w")
    

    #Write it to targetfile
    for single_file in source_files_array:
    	schrift=single_file+"\t"+str(check_file_if_portfolio(single_file))
    	target_filehandle.write(schrift+"\n")
    	print(schrift)

    #Schließe Filehandle    
    target_filehandle.close()



    print("Alle Dateien geprüft!")




if __name__ == "__main__":
    main()

