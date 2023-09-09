import cv2
import numpy as np


# Define the class labels and colors
LABELS = ["person"]
COLORS = [[0, 255, 0]]

# Load the YOLOv8 model
net = cv2.dnn.readNet("yolov8.weights", "yolov8.cfg")

# Load the video
video = cv2.VideoCapture("input.mp4")

while True:
    # Read a frame from the video
    grabbed, frame = video.read()

    # If the frame was not grabbed, then we have reached the end of the video
    if not grabbed:
        break

    # Prepare the frame for processing
    (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # Pass the blob through the network and obtain the detections
    net.setInput(blob)
    layerOutputs = net.forward(["yolo_82", "yolo_94", "yolo_106"])

    # Initialize the lists of detections
    boxes = []
    confidences = []
    classIDs = []

    # Loop over each of the layer outputs
    for output in layerOutputs:
        # Loop over each of the detections
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # Filter out weak detections
            if confidence > 0.5:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confident.append(float(confidence))
                classIDs.append(classID)

    # Apply non-maxima suppression to suppress weak, overlapping detections
    idxs = cv2.dnn.NMSBoxes(boxes, confident, 0.5, 0.3)

    # Ensure at least one detection exists
    if len(idxs) > 0:
        # Loop over the indexes we are keeping
        for i in idxs.flatten():
            # Extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            # Draw a bounding box rectangle and label on the image
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]], confident[i])
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            # Show the output image
            cv2.imshow("Image", frame)
            key = cv2.waitKey(1) & 0xFF

            # If the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
video.release()
cv2.destroyAllWindows()