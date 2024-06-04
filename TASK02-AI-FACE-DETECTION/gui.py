import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import main

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection and Recognition")
        
        self.create_widgets()
        self.imgtk = None  # Store reference to the image

    def create_widgets(self):
        # Creating a frame for the controls
        control_frame = tk.Frame(self.root, bg='lightgrey', padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        
        # Adding label
        self.label = tk.Label(control_frame, text="Select an image to recognize faces:", bg='lightgrey', font=('Arial', 12))
        self.label.pack(side=tk.LEFT, padx=5)
        
        # Adding Select Image button
        self.btn_select = tk.Button(control_frame, text="Select Image", command=self.select_image, bg='blue', fg='white', font=('Arial', 12))
        self.btn_select.pack(side=tk.LEFT, padx=5)
        
        # Adding Clear button
        self.btn_clear = tk.Button(control_frame, text="Clear", command=self.clear_canvas, bg='red', fg='white', font=('Arial', 12))
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        
        # Adding canvas for image display
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        try:
            image, results = main.recognize_faces(file_path)
            
            # Convert image to PIL format
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(image_rgb)
            
            # Resize image to fit within the canvas while maintaining aspect ratio
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            pil_image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

            # Resize canvas to fit the image
            self.canvas.config(width=pil_image.width, height=pil_image.height)
            
            # Convert PIL image to ImageTk format
            self.imgtk = ImageTk.PhotoImage(image=pil_image)
            
            # Update canvas with the new image
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imgtk)
            
            # Display results
            if results:
                result_text = "\n".join([f"{name}" for _, _, _, _, name in results])
                messagebox.showinfo("Recognition Results", result_text)
            else:
                messagebox.showinfo("Recognition Results", "No faces recognized.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.imgtk = None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Set initial window size
    app = FaceRecognitionApp(root)
    root.mainloop()

