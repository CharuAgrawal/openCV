# cap = cv2.VideoCapture('Videos/noisy_video.mp4')
import cv2

# Open the video file
cap = cv2.VideoCapture('Videos/noisy_video.mp4')

# Get the total number of frames
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Read the first few frames to initialize the denoising process
frames = []
for i in range(5):
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray_frame)

# Create a VideoWriter object to save the denoised video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('denoised_video.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (frames[0].shape[1], frames[0].shape[0]), False)

# Process the video frame by frame
for i in range(5, frame_count):
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray_frame)
    
    # Ensure the temporal window size is odd
    temporal_window_size = 5  # Must be odd and less than or equal to the number of frames

    # Apply temporal denoising with odd window sizes
    denoised_frame = cv2.fastNlMeansDenoisingMulti(frames, len(frames) // 2, temporal_window_size, None, 3, 7, 21)
    
    # Write the denoised frame to the output video
    out.write(denoised_frame)
    
    # Display the denoised frame
    cv2.imshow('Denoised Frame', denoised_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Remove the oldest frame to maintain the window size
    frames.pop(0)

# Release the video objects
cap.release()
out.release()
cv2.destroyAllWindows()
