import csv, json, os, sys

typeFile = "train"
# typeFile = "test"
csvPath = fr"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\{typeFile}\_annotations.csv"
classesPath = fr"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\classes.json"
outputPath = fr"C:\Users\livin\Desktop\portfolio\AI\dataset\face_mask210319\roboflow_Mask_v4_raw_tensorflow\{typeFile}"
lstClasses = []
lstFiles = []

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
            # print(row["filename"], row["width"], row["height"], row["class"], row["xmin"], row["ymin"], row["xmax"], row["ymax"])
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
            
            # 如果是第一次寫入看到已經有相同檔案，就刪掉。第二次以後用append的方式寫入
            if outputFileName not in lstFiles:
              lstFiles.append(outputFileName)
              if os.path.isfile(outputFileName):
                os.remove(outputFileName)
                print(outputFileName)
            
            with open(outputFileName, "a") as f_w:
              f_w.write(f"{classIndex} {centerX:.6f} {centerY:.6f} {regularization_w:.6f} {regularization_h:.6f} \n")
  
  except ValueError as e:
    print("Decoding JSON has failed: ", e)
  except OSError as e:
    print("Could not open/read file: ", e)
    sys.exit()
  
  print("Done!")
