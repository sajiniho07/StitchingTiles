import os
import numpy as np
import pydicom
from m2stitch import stitch_images
from pydicom.pixel_data_handlers import apply_voi_lut
from PIL import Image

def read_dcm_images_from_directory(directory_path):
    image_files = [f for f in os.listdir(directory_path) if f.endswith(".dcm")]
    if not image_files:
        print("No DICOM files found in the directory.")
        return None
    dcm_images = []
    for file_name in image_files:
        file_path = os.path.join(directory_path, file_name)
        try:
            dataset = pydicom.dcmread(file_path)
            image_array = apply_voi_lut(dataset.pixel_array, dataset)
            dcm_images.append(image_array)
        except Exception as e:
            print(f"Error reading '{file_name}': {e}")
    return dcm_images

def calculate_position_indices(images):
    num_images = len(images)
    image_shape = images[0].shape
    position_indices = np.zeros((num_images, len(image_shape)), dtype=int)
    for i in range(num_images):
        indices = np.unravel_index(i, image_shape)
        position_indices[i] = indices
    return position_indices

input_dir = "res"
dicom_images = read_dcm_images_from_directory(input_dir)
position_indices = calculate_position_indices(dicom_images)

stitched_result, _ = stitch_images(images=dicom_images, position_indices=position_indices, ncc_threshold=0.3)

stitched_image = Image.fromarray(stitched_result.astype(np.uint8))
stitched_image.save('output_m2stitch.jpg')
