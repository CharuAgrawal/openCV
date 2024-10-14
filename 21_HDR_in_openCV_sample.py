import cv2 as cv
import numpy as np


# List of exposure images
img_files = ["Photos/fan0000_167.tif", "Photos/fan0000_1667.tif", "Photos/fan0000_3334.tif", "Photos/fan0000_8334.tif"] # "Photos/fan0000_16667.tif"]
img_list = [cv.imread(fn) for fn in img_files]

# Exposure times in seconds
exposure_times = np.array([0.00167, 0.01667, 0.0333, 0.08334], dtype=np.float32)


# Merge exposures to HDR image
merge_debevec = cv.createMergeDebevec()
hdr_debevec = merge_debevec.process(img_list, times=exposure_times.copy())


# Tonemap HDR image
tonemap= cv.createTonemap(2.2)
# tonemap = cv.createTonemapDurand(gamma=2.2)
ldr = tonemap.process(hdr_debevec.copy())

# Convert to 8-bit image
ldr_8bit = np.clip(ldr * 255, 0, 255).astype('uint8')


# Save the result
cv.imwrite("ldr_image.jpg", ldr_8bit)

# Display the result
cv.imshow("LDR Image", ldr_8bit)
cv.waitKey(0)
cv.destroyAllWindows()
