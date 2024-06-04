
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.recommend import recommend

def get_recommendations():
    user_id = user_id_entry.get().strip()
    if user_id.isdigit():
        user_id = int(user_id)
        recommendations = recommend(user_id)
        recommendation_table.delete(*recommendation_table.get_children())
        if recommendations is not None:
            if not recommendations.empty:
                for idx, movie in recommendations.iterrows():
                    recommendation_table.insert("", "end", values=(movie['title'],))
            else:
                recommendation_table.insert("", "end", values=("No recommendations available",))
        else:
            messagebox.showinfo("Info", "User ID does not exist.")
    else:
        # Clear the recommendation table
        recommendation_table.delete(*recommendation_table.get_children())
        # Show error message for invalid user ID
        messagebox.showerror("Error", "Invalid user ID. Please enter a valid user ID.")

# Create the main application window
root = tk.Tk()
root.title("Movie Recommendation System")

# Center the window horizontally
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# Create a frame for user input
input_frame = ttk.Frame(root, padding="20")
input_frame.pack(fill="x", pady=(20, 10))

# Create input widgets
user_id_label = ttk.Label(input_frame, text="Enter User ID:", font=('Arial', 12))
user_id_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))

user_id_entry = ttk.Entry(input_frame, width=10, font=('Arial', 12))
user_id_entry.grid(row=0, column=1, padx=(0, 10))

# Create a frame for buttons
button_frame = ttk.Frame(input_frame)
button_frame.grid(row=0, column=2, columnspan=2, padx=(10, 0), sticky="ew")

recommend_button = tk.Button(button_frame, text="Recommend Movies", command=get_recommendations, bg='blue', fg='white', font=('Arial', 12))
recommend_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=lambda: user_id_entry.delete(0, tk.END), bg='red', fg='white', font=('Arial', 12))
clear_button.pack(side=tk.LEFT, padx=5)

# Create a frame for displaying recommendations
output_frame = ttk.Frame(root, padding="20")
output_frame.pack(fill="both", expand=True)

# Create a treeview for displaying recommendations
recommendation_table = ttk.Treeview(output_frame, columns=("Title",), show="headings", height=10)
recommendation_table.heading("Title", text="Title")
recommendation_table.pack(fill="both", expand=True)

# Start the Tkinter event loop
root.mainloop()



