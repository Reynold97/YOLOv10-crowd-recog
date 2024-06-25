from ultralytics import YOLOv10
import cv2
import supervision as sv

# Load the model
model = YOLOv10('weights/yolov10n.pt')

# Read the input image
image = cv2.imread('data/example_1.jpg')

# Perform object detection
results = model([image])

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    #result.show()  # display to screen
    result.save(filename="data/annotated_example_1.jpg")  # save to disk

for r in boxes:
    print(r.cls)   # print the class  0 is the label for persons and 56 is the label for chairs
    print(r.conf)  # print the confiability value
    print(r.xyxy)  # print boxes as xy format


#Using supervision 
'''
# Convert Ultralytics results to Supervision Detections
detections = sv.Detections.from_ultralytics(results)

# Initialize annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Annotate the image with bounding boxes and labels
annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

# Save the annotated image
output_filename = 'data/annotated_example_1.jpg'
cv2.imwrite(output_filename, annotated_image)

# Optionally, display the image
sv.plot_image(annotated_image)
'''