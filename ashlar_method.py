import subprocess
import os
import glob
from PIL import Image
import pydicom
import shutil

def get_image_size(path):
    with Image.open(path) as tiff:
        return tiff.size

def convert_dicom_to_tiff(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    tiff_files = []

    for idx, dicom_file in enumerate(glob.glob(os.path.join(input_dir, "*.dcm")), start=1):
        try:
            ds = pydicom.dcmread(dicom_file)
            tiff_file = os.path.splitext(os.path.basename(dicom_file))[0] + ".tif"
            tiff_path = os.path.join(output_dir, tiff_file)
            
            image = Image.fromarray(ds.pixel_array)
            image.save(tiff_path)
            tiff_files.append(tiff_path)

        except Exception as e:
            print(f"Error processing '{dicom_file}': {e}")

    return tiff_files

def merge_tiff_files(files_dir, output_dir, tiff_files, overlap=0.15, width=10, height=10):
    tiff_output = os.path.join(output_dir, "output.ome.tif")
    
    tiff_command = [
        "ashlar",
        "-o",
        tiff_output,
        f"fileseries|{files_dir}" +  "|pattern=img4_{series:1}.tif" + f"|overlap={overlap}|width={width}|height={height}|direction=horizontal",
    ]
    tiff_command.extend(tiff_files)
    tiff_command.append("--filter-sigma")
    tiff_command.append("1")

    try:
        subprocess.run(tiff_command, check=True)
        convert_to_jpeg_and_save_output(output_dir, tiff_output)
        print("Merged image saved as JPEG successfully.")
    except subprocess.CalledProcessError as e:
        print("Error while running ashlar:", e)

def convert_to_jpeg_and_save_output(output_dir, tiff_output):
    with Image.open(tiff_output) as tiff_image:
        tiff_image_8bit = tiff_image.convert("L")

    jpeg_output = os.path.join(output_dir, "output_ashlar.jpg")
    tiff_image_8bit.save(jpeg_output, "JPEG")

def main():
    input_dir = "res"
    output_dir = ""
    temp_dir = os.path.join(input_dir, "temp_tiff_output")

    tiff_files = convert_dicom_to_tiff(input_dir, temp_dir)
    width, height = get_image_size(tiff_files[-1])

    merge_tiff_files(temp_dir, output_dir, tiff_files, overlap=0.15, width=width, height=height)

    # Clean up: Delete the temporary directory and its contents
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
