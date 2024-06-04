import face_recognition
import pandas as pd
import cv2
import numpy as np

# Load student data
students_df = pd.read_csv('players.csv')

# Create a dictionary to store face encodings
student_encodings = {}

for index, row in students_df.iterrows():
    image_path = f"photos/{row['photo']}"
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    student_encodings[row['name']] = {
        'encoding': face_encoding
    }

def recognize_faces(input_image_path):
    # Load the input image
    input_image = face_recognition.load_image_file(input_image_path)
    
    # Detect faces in the input image
    face_locations = face_recognition.face_locations(input_image)
    face_encodings = face_recognition.face_encodings(input_image, face_locations)
    
    # Convert the image to BGR for OpenCV
    input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
    
    # Initialize results
    results = []

    # Loop over each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Find the best match for the detected face
        matches = face_recognition.compare_faces([student['encoding'] for student in student_encodings.values()], face_encoding)
        face_distances = face_recognition.face_distance([student['encoding'] for student in student_encodings.values()], face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            matched_name = list(student_encodings.keys())[best_match_index]
            
            # Add result to the list
            results.append((top, right, bottom, left, matched_name))
            
            # Draw a box around the face
            cv2.rectangle(input_image, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Draw a label with the student's name
            label = f"{matched_name}"
            cv2.putText(input_image, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return input_image, results

def show_image(image):
    # Show the result
    cv2.imshow('Face Recognition', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage
    input_image_path = 'input.jpg'  # Path to the input image
    image, results = recognize_faces(input_image_path)
    show_image(image)
