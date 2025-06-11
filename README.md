📸 Facial Recognition Attendance System
This Python project is a real-time face recognition-based attendance system. It uses your webcam to detect and recognize known faces and automatically marks attendance in an Excel spreadsheet.

✅ Features:
🔍 Detects and recognizes faces using the webcam.
🧠 Trains on face encodings from a local image dataset.
📅 Records daily attendance into an Excel file (attendance.xlsx).
🚫 Avoids duplicate attendance entries per session.
📊 GUI to view attendance records using a simple table interface.

📁 Folder Structure:
facial_attendance
 --- facial_attendance.py     # Main script
 --- image folder/            # Subfolders named after each person, containing their images
 --- attendance.xlsx          # Auto-generated attendance sheet


🛠️ Technologies Used:
OpenCV – for video capture and display.
face_recognition – for facial detection and recognition.
NumPy – for numerical operations.
Pandas – for spreadsheet manipulation.
Tkinter – for GUI to view attendance.


🧪 How It Works

1)Training Phase:
-The script scans the image folder, where each subfolder is a person's name.
-It processes all images inside each folder and computes face encodings.
-A mean encoding is calculated per person to improve recognition accuracy.

2)Recognition Phase:
-Starts webcam stream and captures frames in real time.
-Detects faces and compares them with the trained encodings.
-If a match is found, marks the name as "Present" for the current date in the Excel sheet.

3)Attendance GUI:
After closing the webcam window, a simple GUI window opens to display the attendance table
🧾 Output Example (Excel File)
Serial Number 	Name	  11-06-2025
1	            vinodh    	Present
2	            mani       	Absent


▶️ How to Run
1)Install dependencies:
pip install opencv-python face_recognition pandas openpyxl

2)Add training images in the format:
 image folder
 ├── vinodh
 │   ├── img1.jpg
 │   └── img2.jpg
 └── mani
     ├── img1.jpg

3)Run the script:
python facial_attendance.py

4)Press q to stop attendance capture. The attendance window will appear next.

📌 Note:
-Accuracy improves with high-resolution, front-facing images in the training set.
-Avoid using blurred or dark images for training.
-Only one instance of a person is marked "Present" per session.



🧑‍💻 Author
Vinodhkondaveeti

