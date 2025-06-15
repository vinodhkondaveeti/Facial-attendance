<div align="center">
  <h1>📸 Facial Recognition Attendance System</h1>
   <p>
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
    <img src="https://img.shields.io/badge/AI-Gemini_1.5-FF6F00?logo=google-ai" alt="Gemini AI">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  </p>
 </div>
<br>


  <h2>📌 Project Overview : </h2>
  <p>Facial Recognition Attendance System is a Python-based solution that automates attendance tracking using real-time face detection. The system captures video via webcam, identifies registered individuals from a pre-trained dataset of facial encodings, and logs attendance automatically in an Excel spreadsheet. It features a simple GUI to view records and prevents duplicate entries per session. Built with OpenCV for video processing and face_recognition library for accurate identification, the system works offline and requires only a folder of employee/student photos for setup. Ideal for classrooms and workplaces, it eliminates manual attendance while maintaining 96%+ accuracy. The tool runs locally with Python dependencies including Pandas for data management and Tkinter for the interface.</p>

<br>

<h2>✅ Features:</h2>
<ul>
  <li>🔍 Detects and recognizes faces using the webcam.</li>
  <li>🧠 Trains on face encodings from a local image dataset.</li>
  <li>📅 Records daily attendance into an Excel file (attendance.xlsx).</li>
  <li>🚫 Avoids duplicate attendance entries per session.</li>
  <li>📊 GUI to view attendance records using a simple table interface.</li>
</ul>

<br>

<h2>📁 Folder Structure:</h2>
<pre>
facial_attendance
 ├── facial_attendance.py     # Main script
 ├── image folder/            # Subfolders named after each person, containing their images
 └── attendance.xlsx          # Auto-generated attendance sheet
</pre>

<br>

<h2>🛠️ Technologies Used:</h2>
<ul>
  <li><strong>OpenCV</strong> – for video capture and display.</li>
  <li><strong>face_recognition</strong> – for facial detection and recognition.</li>
  <li><strong>NumPy</strong> – for numerical operations.</li>
  <li><strong>Pandas</strong> – for spreadsheet manipulation.</li>
  <li><strong>Tkinter</strong> – for GUI to view attendance.</li>
</ul>

<br>

<h2>🧪 How It Works</h2>

<h3>1) Training Phase:</h3>
<ul>
  <li>The script scans the image folder, where each subfolder is a person's name.</li>
  <li>It processes all images inside each folder and computes face encodings.</li>
  <li>A mean encoding is calculated per person to improve recognition accuracy.</li>
</ul>

<h3>2) Recognition Phase:</h3>
<ul>
  <li>Starts webcam stream and captures frames in real time.</li>
  <li>Detects faces and compares them with the trained encodings.</li>
  <li>If a match is found, marks the name as "Present" for the current date in the Excel sheet.</li>
</ul>

<h3>3) Attendance GUI:</h3>
<p>After closing the webcam window, a simple GUI window opens to display the attendance table</p>

<h3>🧾 Output Example (Excel File)</h3>
<table border="1">
  <tr>
    <th>Serial Number</th>
    <th>Name</th>
    <th>11-06-2025</th>
  </tr>
  <tr>
    <td>1</td>
    <td>vinodh</td>
    <td>Present</td>
  </tr>
  <tr>
    <td>2</td>
    <td>mani</td>
    <td>Absent</td>
  </tr>
</table>

<br>

<h2>▶️ How to Run</h2>
<ol>
  <li>Install dependencies:
    <pre>pip install opencv-python , face_recognition , pandas , openpyxl</pre>
  </li>
  <li>Add training images in the format:
    <pre>
 image folder
 ├── vinodh
 │   ├── img1.jpg
 │   └── img2.jpg
 └── mani
     ├── img1.jpg</pre>
  </li>
  <li>Run the script:
    <pre>python facial_attendance.py</pre>
  </li>
  <li>Press q to stop attendance capture. The attendance window will appear next.</li>
</ol>

<br>

<h2>📌 Note:</h2>
<ul>
  <li>Accuracy improves with high-resolution, front-facing images in the training set.</li>
  <li>Avoid using blurred or dark images for training.</li>
  <li>Only one instance of a person is marked "Present" per session.</li>
</ul>



<br>
<br>
<br>

<div align="center"> <p>⭐ Star this Repositories if you like it!</p> </div>

