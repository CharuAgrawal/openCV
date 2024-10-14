import cv2
import vpi
import numpy as np

# Open the video file
cap = cv2.VideoCapture('Vidoes/noisy_video.mp4')

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the denoised video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('denoised_video.mp4', fourcc, fps, (frame_width, frame_height), False)

# Create a VPI stream
stream = vpi.Stream()

# Create a VPI Temporal Noise Reduction object
tnr = vpi.TemporalNoiseReduction((frame_width, frame_height), vpi.Format.NV12_ER)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to NV12 format
    nv12_frame = vpi.asimage(frame).convert(vpi.Format.NV12_ER)
    
    # Apply temporal noise reduction
    denoised_frame = tnr(nv12_frame, preset=vpi.TNRPreset.INDOOR_MEDIUM_LIGHT, strength=0.5)
    
    # Convert denoised frame to RGB for saving
    denoised_rgb = denoised_frame.convert(vpi.Format.RGB8)
    
    # Write the denoised frame to the output video
    out.write(denoised_rgb.cpu())

    # Display the denoised frame
    cv2.imshow('Denoised Frame', denoised_rgb.cpu())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video objects
cap.release()
out.release()
cv2.destroyAllWindows()
