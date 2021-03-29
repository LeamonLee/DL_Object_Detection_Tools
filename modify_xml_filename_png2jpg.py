import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv_v2(path):
    
    for xml_file in glob.glob(path + r'\*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        objFilename = root.find('filename')
        print("Original fileName: ", objFilename.text)
        objFilename.text = objFilename.text[:-3] + 'jpg'
        print("Modified fileName: ", objFilename.text)
        tree.write(xml_file)


if __name__ == '__main__':

    path = r"C:\Users\leamon.lee\Downloads\face_mask\kaggle_dataset\annotations\test"
    xml_to_csv_v2(path)
