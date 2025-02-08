import os

def list_files_in_folder(folder_path):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        
        # Create or open a text file to write the file names
        with open('Story.txt', 'w') as txt_file:
            for file_name in files:
                # Write each file name to the text file
                last = file_name[-4:]
                print(last)
                if(last != ".txt"):
                    continue
                #check if it is txt file, then continue
                rest = file_name[:-4]
                if(rest == "default"):
                    continue
                #check if it is default, then ingnore
                txt_file.write(rest + '\n')
        
        print(f"File list written to 'file_list.txt' successfully.")
    
    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' does not exist.")
        os.makedirs()
        #trying again
        list_files_in_folder(folder_path)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the folder path here
folder_path = 'Story'

# Call the function with the specified folder path
list_files_in_folder(folder_path)
