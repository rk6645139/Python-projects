import threading
import cv2
from deepface import DeepFace


cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
counter =0
face_match = False
reference_img=cv2.imread("face_recognition/WIN_20241108_11_58_16_Pro.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match =True

        else:
            face_match=False
    except ValueError:
        face_match=False

while True:
    ret, frame=cap.read()

    if ret:
        if counter %30==0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter+=1


        if face_match:
            cv2.putText(frame, "Match!!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        else:
            cv2.putText(frame, "No Match!!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)


    key= cv2.waitKey(1)

    if key==ord("q"):
        break

cv2.destroyAllWindows()
#successful match worked



# import threading
# import cv2
# from deepface import DeepFace
# import time

# # Initialize the video capture and set resolution
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# # Load the reference image and DeepFace model once to avoid reloading
# reference_img = cv2.imread("face_recognition/WIN_20241108_11_58_16_Pro.jpg")
# model_name = 'VGG-Face'  # Specify the model once for consistency and speed

# # Shared variables for threading
# face_match = False
# processing = False

# def check_face(frame):
#     global face_match, processing
#     try:
#         # Run verification and update the face_match variable
#         result = DeepFace.verify(frame, reference_img.copy(), model_name=model_name)
#         face_match = result['verified']
#     except ValueError:
#         face_match = False
#     processing = False  # Allow new thread to start

# # Main loop
# while True:
#     ret, frame = cap.read()

#     if ret:
#         # Check the face every 30 frames (approximately 1 second)
#         if not processing:
#             processing = True
#             threading.Thread(target=check_face, args=(frame.copy(),)).start()

#         # Display match result on the frame
#         if face_match:
#             cv2.putText(frame, "Match!!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         else:
#             cv2.putText(frame, "No Match!!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#         # Show the video feed
#         cv2.imshow("Video", frame)

#     # Exit the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()

"""
import cv2
import face_recognition
import numpy as np

def facial_recognition():
    # Load known faces (replace these with paths to your own images)
    known_face_encodings = []
    known_face_names = []

    # Example: Load a few known faces
    # You'll need to replace these with actual images of people you want to recognize
    known_images = [
        ("/path/to/person1.jpg", "Person 1"),
        ("/path/to/person2.jpg", "Person 2")
    ]

    # Encode known faces
    for image_path, name in known_images:
        try:
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(name)
        except Exception as e:
            print(f"Error loading {name}'s image: {e}")

    # Start video capture
    video_capture = cv2.VideoCapture(0)  # 0 for default camera

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the image from BGR color to RGB
        rgb_frame = frame[:, :, ::-1]

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the lowest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Facial Recognition', frame)

        # Hit 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    facial_recognition()
"""