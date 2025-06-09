import cv2
import os
import numpy as np
import face_recognition
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

MAIN_FOLDER = "C:/Users/VINOD/Desktop/projects/facial attendence/image folder"
SPREADSHEET = "C:/Users/VINOD/Desktop/projects/facial attendence/attendance.xlsx"

def train_model():
    encodings = {}
    for sub_folder in os.listdir(MAIN_FOLDER):
        path = os.path.join(MAIN_FOLDER, sub_folder)
        if os.path.isdir(path):
            known_encodings = []
            for img_name in os.listdir(path):
                if img_name.endswith(('png', 'jpg', 'jpeg')):
                    image_path = os.path.join(path, img_name)
                    image = face_recognition.load_image_file(image_path)
                    encoding = face_recognition.face_encodings(image)
                    if encoding:
                        known_encodings.append(encoding[0])
            if known_encodings:
                encodings[sub_folder] = np.mean(known_encodings, axis=0)
    return encodings

face_db = train_model()

def update_spreadsheet(name):
    date = datetime.now().strftime('%d-%m-%Y')
    if not os.path.exists(SPREADSHEET):
        df = pd.DataFrame(columns=["Serial Number", "Name", date])
        for idx, folder in enumerate(face_db.keys(), start=1):
            df = pd.concat([df, pd.DataFrame([[idx, folder, "Absent"]], columns=df.columns)], ignore_index=True)
        df.to_excel(SPREADSHEET, index=False, engine='openpyxl')
    
    df = pd.read_excel(SPREADSHEET, engine='openpyxl')
    if date not in df.columns:
        df[date] = "Absent"
    if name in df["Name"].values:
        df.loc[df["Name"] == name, date] = "Present"
    df.to_excel(SPREADSHEET, index=False, engine='openpyxl')

def recognize_face():
    cap = cv2.VideoCapture(0)
    marked_names = set()  # To avoid duplicate entries per session

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)

        for face_location, encoding in zip(faces, encodings):
            matches = face_recognition.compare_faces(list(face_db.values()), encoding, tolerance=0.4)  # Tighter threshold
            face_distances = face_recognition.face_distance(list(face_db.values()), encoding)
            best_match_index = np.argmin(face_distances) if face_distances.size else None

            name = "Unknown"
            if best_match_index is not None and matches[best_match_index]:
                name = list(face_db.keys())[best_match_index]

                if name not in marked_names:
                    update_spreadsheet(name)
                    marked_names.add(name)

            # Draw rectangle and label
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"{name}", (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0) if name != "Unknown" else (0, 0, 255), 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def show_attendance_ui():
    root = tk.Tk()
    root.title("Attendance Records")
    tree = ttk.Treeview(root)
    df = pd.read_excel(SPREADSHEET, engine='openpyxl')
    tree["columns"] = list(df.columns)

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack(expand=True, fill='both')
    root.mainloop()

def main():
    recognize_face()
    show_attendance_ui()

if __name__ == "__main__":
    main()
