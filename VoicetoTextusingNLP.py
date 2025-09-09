import speech_recognition as sr
import mysql.connector

#  MySQL Connection 
conn = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="mygominds12345678", 
    database="school"  
)
cursor = conn.cursor()

# Voice Recognition 
recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print(" Say the Student ID clearly...")
    recognizer.adjust_for_ambient_noise(source)  
    audio = recognizer.listen(source)

try:
    # Convert speech to text
    student_id = recognizer.recognize_google(audio)
    print(f" Recognized Student ID: {student_id}")

    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()

    if result:
        print("Student Details:", result)
    else:
        print(" No student found with this ID.")

except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print(f"Google Speech Recognition service error: {e}")
