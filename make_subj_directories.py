# Made by [@SinghArindam](https://github.com/SinghArindam/)

import os

def create_subject_folders(subjects, subfolders):
    """
    Creates folders for each subject and subfolders within them, in the current directory.
    
    Args:
        subjects (list): List of subjects for which folders will be created.
        subfolders (list): List of subfolders to create within each subject folder.
    """
    for subject in subjects:
        # Create the subject folder path
        subject_path = os.path.join(".",subject)
        
        # Check if the subject folder exists, if not, create it
        if not os.path.exists(subject_path):
            os.makedirs(subject_path)
            print(f"Created folder: {subject_path}")
        else:
            print(f"Folder already exists: {subject_path}")
        
        # Create subfolders within the subject folder
        for subfolder in subfolders:
            subfolder_path = os.path.join(subject_path, subfolder)
            
            # Check if the subfolder exists, if not, create it
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"  Created subfolder: {subfolder_path}")
            else:
                print(f"  Subfolder already exists: {subfolder_path}")

# Example usage
subjects = [
            "EC302 VLSI Design", 
            "EC304 Digital Signal Processing", 
            "EC306 Embedded Systems",
            "EC332 Information Theory and Coding", 
            "SE206 Database Management Systems", 
            "CO328 Deep Learning",
            "MG302 Fundamentals of Management"
            ]
subfolders = ["Notes", "Assignments", "PYQs", "Books", "Practicals", "Videos"]

create_subject_folders(subjects, subfolders)
