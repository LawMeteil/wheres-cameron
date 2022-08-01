import os,time,cv2
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image, ImageDraw, ImageFont

API_KEY = 'bcdef1c39ab04fb08d9591e57fd820e6'
ENDPOINT = 'https://sbai-sdc-iart.cognitiveservices.azure.com/'
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

# path_img =
# path_vid =

def process(path_img,path_vid):
    response_face_source = detect(path_img)
    face_src = response_face_source[0].face_id
    date = time.strftime("%Y-%m-%dT%I%M%S")
    
    os.mkdir(date)
    cap= cv2.VideoCapture(path_vid)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        # EXTRACT
        n_frame=str(i)+'.jpg'
        os.chdir(date)
        cv2.imwrite(n_frame,frame)
        response_detected_faces = detect(n_frame)
        faces = [face.face_id for face in response_detected_faces]

        matched_faces = match(face_src,faces)
        img = Image.open(open(n_frame, 'rb'))
        # RECTANGLE
        img = Image.open(open(n_frame, 'rb'))
        draw = ImageDraw.Draw(img)
        undetected=True
        for matched_face in matched_faces:
            for face in response_detected_faces:
                if face.face_id == matched_face.face_id:
                    # RECT
                    rect = face.face_rectangle
                    left = rect.left
                    top = rect.top
                    right = rect.width + left
                    bottom = rect.height + top
                    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
                    # img.show()
                    undetected=False
        if(undetected):
            os.remove(n_frame)
        i+=1
        os.chdir('..')


# cap.release()
# cv2.destroyAllWindows()
    
# DETECT FACES
def detect(frame):
    return face_client.face.detect_with_stream(
        image=open(frame, 'rb'),
        detection_model='detection_03',
        recognition_model='recognition_04',  
    )

# MATCH
def match(face_src,faces):
    return face_client.face.find_similar(
        face_id=face_src,
        face_ids=faces
    )

# img = Image.open(open(r'.\group1.jpg', 'rb'))