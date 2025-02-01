# Made by [@SinghArindam](https://github.com/SinghArindam/)

import os
import customtkinter as ctk
from tkinter import messagebox
from CTkListbox import *

placeholder = "Placeholder DO NOT DELETE"

# Function to create subject and subfolder structure
def create_subject_folders(subjects, subfolders, base_folder="."):
    for subject in subjects:
        if subject==placeholder:
            continue
        subject_path = os.path.join(base_folder, subject)
        if not os.path.exists(subject_path):
            os.makedirs(subject_path)

        for subfolder in subfolders:
            if subfolder==placeholder:
                continue
            subfolder_path = os.path.join(subject_path, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

# GUI Class
def gui_app():
    # Initialize CustomTkinter theme
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("dark-blue")

    # Initialize main application window
    app = ctk.CTk()
    app.title("Semester-Wise Folder Creater/Organizer by SinghArindam")
    app.geometry("700x500")

    # Subject and Subfolder lists
    subjects = [
        placeholder,
        "EC302 VLSI Design", 
        "EC304 Digital Signal Processing", 
        "EC306 Embedded Systems",
        "EC332 Information Theory and Coding", 
        "SE206 Database Management Systems", 
        "CO328 Deep Learning",
        "MG302 Fundamentals of Management"
        ]
    subfolders = [
        placeholder,
        "Notes", 
        "Assignments", 
        "PYQs", 
        "Books", 
        "Practicals", 
        "Videos"
        ]

    def add_subject():
        subject = subject_entry.get()
        if subject and subject not in subjects:
            subjects.append(subject)
            subject_listbox.insert(ctk.END, subject)
            subject_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Subject is empty or already exists!")

    def delete_subject():
        selected = subject_listbox.curselection()
        if selected:
            subject = subject_listbox.get(selected)
            subjects.remove(subject)
            subject_listbox.delete(selected)
        else:
            messagebox.showerror("Error", "No subject selected!")

    def add_subfolder():
        subfolder = subfolder_entry.get()
        if subfolder and subfolder not in subfolders:
            subfolders.append(subfolder)
            subfolder_listbox.insert(ctk.END, subfolder)
            subfolder_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Subfolder is empty or already exists!")

    def delete_subfolder():
        selected = subfolder_listbox.curselection()
        if selected:
            subfolder = subfolder_listbox.get(selected)
            subfolders.remove(subfolder)
            subfolder_listbox.delete(selected)
        else:
            messagebox.showerror("Error", "No subfolder selected!")

    def create_folders():
        base_folder = base_folder_entry.get()
        if not base_folder:
            user_choice = messagebox.askquestion("Are you sure?", "Base folder name is empty!\nAre you sure You want to Continue?\n(This will Create folders in current directory)")
            if user_choice=="no":
                return
            base_folder = "."

        if not os.path.exists(base_folder):
            os.makedirs(base_folder)

        if subjects and subfolders:
            create_subject_folders(subjects, subfolders, base_folder)
            messagebox.showinfo("Success", "Folders created successfully!")
        else:
            messagebox.showerror("Error", "Subjects or Subfolders list is empty!")

    def refresh_subject_list():
        subject_listbox.delete(0, ctk.END)
        for subject in subjects:
            subject_listbox.insert(ctk.END, subject)

    def refresh_subfolder_list():
        subfolder_listbox.delete(0, ctk.END)
        for subfolder in subfolders:
            subfolder_listbox.insert(ctk.END, subfolder)

    def toggle_theme():
        theme = theme_switch_var.get()
        ctk.set_appearance_mode("dark" if theme else "light")

    # TOP Frame
    top_frame = ctk.CTkFrame(app)
    top_frame.pack(pady=10, padx=10, fill="both", expand=True)
    ctk.CTkLabel(top_frame, text="\nSemester-Wise Folder Creater/Organizer\n by SinghArindam", font=("Arial", 32)).pack()

    # Subject Frame
    subject_frame = ctk.CTkFrame(app)
    subject_frame.pack(pady=10, padx=10, fill="both", expand=True, side="left")

    ctk.CTkLabel(subject_frame, text="Subjects", font=("Arial", 16)).pack(pady=5)
    subject_entry = ctk.CTkEntry(subject_frame, placeholder_text="Enter subject")
    subject_entry.pack(pady=5)
    ctk.CTkButton(subject_frame, text="Add Subject", command=add_subject).pack(pady=5)
    ctk.CTkButton(subject_frame, text="Delete Subject", command=delete_subject).pack(pady=5)
    ctk.CTkButton(subject_frame, text="Refresh List", command=refresh_subject_list).pack(pady=5)
    subject_listbox = CTkListbox(subject_frame)
    subject_listbox.pack(pady=5)
    refresh_subject_list()

    # Subfolder Frame
    subfolder_frame = ctk.CTkFrame(app)
    subfolder_frame.pack(pady=10, padx=10, fill="both", expand=True, side="left")

    ctk.CTkLabel(subfolder_frame, text="Subfolders", font=("Arial", 16)).pack(pady=5)
    subfolder_entry = ctk.CTkEntry(subfolder_frame, placeholder_text="Enter subfolder")
    subfolder_entry.pack(pady=5)
    ctk.CTkButton(subfolder_frame, text="Add Subfolder", command=add_subfolder).pack(pady=5)
    ctk.CTkButton(subfolder_frame, text="Delete Subfolder", command=delete_subfolder).pack(pady=5)
    ctk.CTkButton(subfolder_frame, text="Refresh List", command=refresh_subfolder_list).pack(pady=5)
    subfolder_listbox = CTkListbox(subfolder_frame)
    subfolder_listbox.pack(pady=5)
    refresh_subfolder_list()

    # Footer Frame
    footer_frame = ctk.CTkFrame(app)
    footer_frame.pack(fill="both", pady=10)

    theme_switch_var = ctk.BooleanVar()
    theme_switch = ctk.CTkSwitch(footer_frame, text="Dark Mode", variable=theme_switch_var, command=toggle_theme)
    theme_switch.pack(padx=10, pady=20)

    base_folder_entry = ctk.CTkEntry(footer_frame, placeholder_text="Enter base folder (e.g., Semester 7)")
    base_folder_entry.pack(padx=10, pady=20)
    
    ctk.CTkButton(footer_frame, text="Create Folders", command=create_folders).pack(padx=10, pady=40)

    # BOTTOM Frame
    bottom_frame = ctk.CTkFrame(app)
    bottom_frame.pack(pady=10, padx=10, fill="both", expand=True)
    ctk.CTkLabel(bottom_frame, text="\nMade by \nSinghArindam", font=("Arial", 16)).pack()
    
    # Run the app
    app.mainloop()

# Run GUI
if __name__ == "__main__":
    gui_app()
