import os
import cv2
import face_recognition

KNOWN_FACES = "known_faces"
UNKNOWN_FACES= "unknown_faces"
TOL=0.6  # Represents the tolerance taken into account in each face-match. The lower the tolerance is,
         # the less likely to get a match
DB_TOL = 0.4 # Float greater that 0 and less or equal than 1. Represents the percentage of pictures from
             # the dataset that should match with the unknown in order to consider it a full match
FR_THICKNESS= 3 #Frame thickness
FONT_THICKNESS= 2
MODEL = "hog" #Alternately "cnn", but it may generate issues on win
MATCH_COLOR = (30,255,0)
UNKNOWN_COLOR = (30,0,240)
known_faces= {}


def drawFaceSquare(image,face_location, color, tag):
    top_left = (face_location[3], face_location[0])
    bottom_right = (face_location[1], face_location[2])
    cv2.rectangle(image, top_left, bottom_right, color, FR_THICKNESS)
        
    top_left = (face_location[3], face_location[2])
    bottom_right = (face_location[1], face_location[2]+20)
    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
    cv2.putText(image, tag, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (190,190,190), thickness = FONT_THICKNESS)


if __name__ == '__main__':
    
    print("Loading dataset")

    for name in os.listdir(KNOWN_FACES):
        known_faces[name] = []
        for file in os.listdir(f"{KNOWN_FACES}/{name}"):
            image = face_recognition.load_image_file(f"{KNOWN_FACES}/{name}/{file}")
            encoding = face_recognition.face_encodings(image)[0]
            known_faces[name].append(encoding)

    print("Processing unknown faces")

    for file in os.listdir(UNKNOWN_FACES):
        print(f"Processing file: {file}")
        image = face_recognition.load_image_file(f"{UNKNOWN_FACES}/{file}")
        face_locations = face_recognition.face_locations(image, model=MODEL)
        face_encodings =face_recognition.face_encodings(image, face_locations)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        
        for face_encoding, face_location in zip(face_encodings,face_locations):
            found=False
            for name in known_faces:
                results = face_recognition.compare_faces(known_faces[name],face_encoding,tolerance=TOL)
                true_amount = sum(results)
                true_coc = true_amount/len(results)*1.0
                if true_coc >= DB_TOL:
                    print(f"Match Found: {name}")
                    drawFaceSquare(image,face_location,MATCH_COLOR,name)
                    found=True
                    break;
            if not found:
                drawFaceSquare(image,face_location,UNKNOWN_COLOR,"Unknown")
        
        cv2.imshow(file, image)
        cv2.waitKey(0)
        cv2.destroyWindow(file)







