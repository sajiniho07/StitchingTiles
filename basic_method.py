import os
import glob
import pydicom
import ashlar
from PIL import Image

dcm_files = glob.glob(os.path.join("res", "*.dcm"))
dcm_files.sort()

# ساخت یک لیست از تصاویر DICOM چون متوجه شدم که آشلار این فرمت رو میخواد 
dcm_images = [pydicom.dcmread(file) for file in dcm_files]

# تبدیل تصاویر DICOM به تصاویر PIL برای ثبت بدون تغییر تایل های ورودی
pil_images = [Image.fromarray(image.pixel_array) for image in dcm_images]

# برای ادغام تصاویر با استفاده از کتابخانه ashlar نیاز به متدی هست که این کتالخانه ندارد
# merged_image = ashlar.....


# ------------------------------------ ادغام تایلها بدون هیچ فیلتری
widths, heights = zip(*(i.size for i in pil_images))

total_width = sum(widths)
max_height = max(heights)

new_image = Image.new('RGB', (total_width, max_height))

x_offset = 0
for image in pil_images:
    new_image.paste(image, (x_offset, 0))
    x_offset += image.width

new_image.save('output_basic.jpg')
