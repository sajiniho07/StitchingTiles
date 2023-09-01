import cv2

def open_and_show_tiff(file_path):
    try:
        image = cv2.imread(file_path)
        if image is not None:
            print(image.shape)
            screen_res = 1200, 600 
            scale = min(screen_res[0] / image.shape[1], screen_res[1] / image.shape[0])

            resized_image = cv2.resize(image, None, fx=scale, fy=scale)

            cv2.imshow("TIFF Image", resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Unable to open or display the TIFF file.")
    except Exception as e:
        print(f"Error opening or displaying the TIFF file: {e}")

tiff_file_path = "output.ome.tif"
# tiff_file_path = "res/temp_tiff_output/img4_1.tif"
open_and_show_tiff(tiff_file_path)
