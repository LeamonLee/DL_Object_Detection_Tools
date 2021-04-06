import os

# typeFile = "train"
typeFile = "test"
imagesPath = fr"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_yolov4\{typeFile}"
outputPath = fr"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_yolov4"
outputFileName = fr"{outputPath}\{typeFile}.txt"


with open(outputFileName, "w") as outfile:
  for filename in os.listdir(imagesPath):
      if filename.endswith(".jpg"):
          outfile.write(f"mydata/{typeFile}/" + filename)
          outfile.write("\n")

print("Done!")

# image_files = []

# for filename in os.listdir(imagesPath):
#     if filename.endswith(".jpg"):
#         image_files.append(f"mydata/{typeFile}/" + filename)

# with open(outputFileName, "w") as outfile:
#     for image in image_files:
#         outfile.write(image)
#         outfile.write("\n")
#     outfile.close()
