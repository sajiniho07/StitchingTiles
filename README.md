# DICOM to TIFF Conversion and Image Stitching

This Python script converts DICOM files into TIFF format, divides them into 1000x1000-pixel pieces, and then stitches them together using the Ashlar tool. Finally, it saves the merged image as a JPEG.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (install via `pip install pydicom Pillow`)
- Ashlar (for image stitching, install via `pip install ashlar`)

## Usage

1. Clone this repository or download the script to your local machine.

2. Organize your DICOM files in a directory (`input_dir`) where each file follows a naming convention like `img_4_1.dcm`, `img_4_2.dcm`, etc.

3. Open the script and customize the following variables at the top according to your needs:

   ```python
   input_dir = "res"  # Directory containing DICOM files
   output_dir = ""    # Output directory for the merged image (leave empty for the current directory)
   ```

4. Run the script using Python:

   ```bash
   python ashlar_method_filepattern.py
   ```

5. The script will perform the following steps:

   - Convert DICOM files to 1000x1000-pixel TIFF pieces.
   - Stitch the TIFF pieces using Ashlar with specified parameters.
   - Save the merged image as `output.ome.tif`.
   - Convert the merged image to an 8-bit JPEG named `output_ashlar.jpg`.

6. The merged image and the JPEG output will be saved in the specified `output_dir` or the current directory.

7. Clean-up: The script will delete the temporary directory (`temp_tiff_output`) and its contents.

## Configuration

You can further configure the stitching process by adjusting the parameters in the script:

- `overlap`: Adjust the overlap value for stitching (default is 0.15).
- `pixel_size`: Set the pixel size according to your image data (default is 0.377454).
- Other Ashlar parameters can be customized within the `tiff_command` list.

## Troubleshooting

If you encounter any issues or errors, please check the error messages in the console for guidance. Ensure that all prerequisites are installed correctly.

## Example

![sample_1](https://github.com/sajiniho07/StitchingTiles/blob/main/output_ashlar.jpg)

## References ##

- https://academic.oup.com/bioinformatics/article/38/19/4613/6668278?login=true

- https://labsyspharm.github.io/ashlar/dataset.html

- https://forum.image.sc/t/ashlar-stitching-questions-and-developments/67418/2

- https://github.com/labsyspharm/ashlar/tree/master

## License ##

Made with :heart: by <a href="https://github.com/sajiniho07" target="_blank">Sajad Kamali</a>

&#xa0;

<a href="#top">Back to top</a>