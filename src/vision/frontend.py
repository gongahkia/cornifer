import cv2
import os
import sight as s
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk


def load_images_from_folder(folder):
    """
    load all images from the specified folder
    """
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            images.append(os.path.join(folder, filename))
    return images


class ImageSelectorApp:
    def __init__(
        self, master, image_folder, image_output_filepath, json_output_filepath
    ):
        self.master = master
        self.master.title("Select an Image")
        self.image_folder = image_folder
        self.image_output_filepath = image_output_filepath
        self.json_output_filepath = json_output_filepath
        self.images = load_images_from_folder(image_folder)
        self.selected_image = None
        self.image_listbox = tk.Listbox(master)
        self.image_listbox.pack(fill=tk.BOTH, expand=True)
        for img in self.images:
            self.image_listbox.insert(tk.END, img)
        self.select_button = tk.Button(
            master, text="Select Image", command=self.select_image
        )
        self.select_button.pack(pady=10)
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def select_image(self):
        """
        handle image selection and call hold_selection_wrapper
        """
        selected_index = self.image_listbox.curselection()
        if selected_index:
            self.selected_image = self.images[selected_index[0]]
            print(f"Selected image: {self.selected_image}")
            try:
                selection_tuple = s.hold_selection_wrapper(
                    self.selected_image,
                    self.image_output_filepath,
                    self.json_output_filepath,
                )
                if selection_tuple[0]:
                    messagebox.showinfo("Success", "Holds selected successfully!")
                else:
                    messagebox.showerror("Error", "Error during hold selection.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please select an image.")


if __name__ == "__main__":
    IMAGE_FOLDER_PATH = "./../corpus/clean/boards_images/"
    IMAGE_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/"
    JSON_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.json"
    root = tk.Tk()
    app = ImageSelectorApp(
        root, IMAGE_FOLDER_PATH, IMAGE_OUTPUT_FILEPATH, JSON_OUTPUT_FILEPATH
    )
    root.mainloop()
