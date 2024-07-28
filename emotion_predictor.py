import cv2
from PIL import Image
import numpy as np
import tensorflow as tf
import pkg_resources

def predict_emotion_from_camera():
    print("Made by Emir Kaan Özdemir.\n")
    print("License: Apache License 2.0\n")
    print("Version: 1.0.0\n")
    print("Please follow me on Github: https://github.com/emirkaanozdemr.\n")
    print("My Hugging Face: https://huggingface.co/emirkaanozdemr. You can find the model in my Hugging Face.\n")
    print("This project is open source. You can contribute to it in my Github. Thank you!\n")
    print("Press 'Enter' to exit.")

    def process_image(input_img):
        if input_img.mode == 'RGBA':
            input_img = input_img.convert('RGB')
        input_img = input_img.resize((170, 170))
        input_img = np.array(input_img)
        input_img = input_img / 255.0
        input_img = np.expand_dims(input_img, axis=0)
        return input_img

    class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

    model_path = pkg_resources.resource_filename(__name__, 'model__version1.0.0__.h5')
    model = tf.keras.models.load_model(model_path)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image = process_image(img)
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)

        cv2.putText(frame, class_names[predicted_class], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Camera', frame)
        print("Made by Emir Kaan Özdemir.\n")
        print("License: Apache License 2.0\n")
        print("Version: 1.0.0\n")
        print("Please follow me on Github: https://github.com/emirkaanozdemr.\n")
        print("My Hugging Face: https://huggingface.co/emirkaanozdemr. You can find the model in my Hugging Face.\n")
        print("This project is open source. You can contribute to it in my Github. Thank you!\n")
        print("Press 'Enter' to exit.")

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
