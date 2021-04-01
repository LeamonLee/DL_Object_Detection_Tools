import csv

csvPath = "C:\Users\leamon.lee\Downloads\face_mask210319\roboflow_Mask_v4_raw_tensorflow\train"


if __name__ == "__main__":

    with open('iris.csv', newline='') as csvfile:
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # 以迴圈輸出指定欄位
        for row in rows:
            print(row['sepal_length'], row['species'])

    xmin = box['xmin']
    xmax = box['xmax']
    ymin = box['ymin']
    ymax = box['ymax']

    xcen = float((xmin + xmax)) / 2 / self.imgSize[1]
    ycen = float((ymin + ymax)) / 2 / self.imgSize[0]

    w = float((xmax - xmin)) / self.imgSize[1]
    h = float((ymax - ymin)) / self.imgSize[0]

    # PR387
    boxName = box['name']
    if boxName not in classList:
        classList.append(boxName)

    classIndex = classList.index(boxName)

    return classIndex, xcen, ycen, w, h