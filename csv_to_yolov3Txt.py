import csv, json, sys

# csvPath = r"C:\Users\leamon.lee\Downloads\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train\_annotations.csv"
# csvPath = r"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train\_annotations.csv"
csvPath = r"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train\extra\1.csv"
classesPath = r"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train\classes.json"
outputPath = r"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train"
lstClasses = []

if __name__ == "__main__":

  try:
    with open(classesPath) as jsonFile:
      dctData = json.load(jsonFile)
      lstClasses = dctData["classes"]

    with open(csvPath, newline='') as csvFile:
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvFile)

        # 以迴圈輸出指定欄位
        # filename,width,height,class,xmin,ymin,xmax,ymax
        for row in rows:
            print(row["filename"], row["width"], row["height"], row["class"], row["xmin"], row["ymin"], row["xmax"], row["ymax"])
            width = int(row["width"])
            height = int(row["height"])
            xmin = int(row["xmin"])
            xmax = int(row["xmax"])
            ymin = int(row["ymin"])
            ymax = int(row["ymax"])

            centerX = (float((xmin + xmax)) / 2) / width
            centerY = (float((ymin + ymax)) / 2) / height

            regularization_w = float((xmax - xmin)) / width
            regularization_h = float((ymax - ymin)) / height
        
            # if row["class"] not in lstClasses:
            #     lstClasses.append(boxName)

            classIndex = lstClasses.index(row["class"])
            filename = row["filename"].rsplit('.')[0]
            outputFileName = outputPath + '\\' + filename + ".txt"
            with open(outputFileName, "r") as f_r:
              lines = f_r.readlines()
              modifyLine = ""
              modifyIdx = 0
              isFound = False
              for line in lines:
                if len(line) > 0:
                  fileClassIndex = line.split()[0]
                  if classIndex == fileClassIndex:
                    isFound = True
                    seekIdx = len(line) - 1
                    modifyLine = line[0:seekIdx] + f"{classIndex} {centerX:.6f} {centerY:.6f} {regularization_w:.6f} {regularization_h:.6f} " + line[-1:]
                    break
              if isFound:
                lines[modifyIdx] = modifyLine
              else:
                lines.append(f"{classIndex} {centerX:.6f} {centerY:.6f} {regularization_w:.6f} {regularization_h:.6f} \n")
              
              with open(outputFileName, "w") as f_w:  
                contents = "".join(lines)
                f_w.write(contents)
  
  except ValueError as e:
    print("Decoding JSON has failed: ", e)
  except OSError as e:
    print("Could not open/read file: ", e)
    sys.exit()
  
  print("Done!")
