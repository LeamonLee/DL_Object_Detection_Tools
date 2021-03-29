import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + r'\*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                        int(root.find('size')[0].text),
                        int(root.find('size')[1].text),
                        member[0].text,
                        int(member[4][0].text),
                        int(member[4][1].text),
                        int(member[4][2].text),
                        int(member[4][3].text)
                    )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def xml_to_csv_v2(path):
    xml_list = []
    for xml_file in glob.glob(path + r'\*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            # print("member.find('name'): ", member.find('name'))
            # print("member.find('bndbox'): ", member.find('bndbox'))
            value = (root.find('filename').text,
                        int(root.find('size')[0].text),
                        int(root.find('size')[1].text),
                        member.find('name').text,
                        int(member.find('bndbox')[0].text),
                        int(member.find('bndbox')[1].text),
                        int(member.find('bndbox')[2].text),
                        int(member.find('bndbox')[3].text)
                    )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def generate_csv_file(path_to_images, path_to_output_csv_file):
    
    xml_df = xml_to_csv_v2(path_to_images)
    xml_df.to_csv(path_to_output_csv_file, index=None)



if __name__ == '__main__':

    # 如果圖片檔和annotation檔放在同個目錄底下可以用這個
    # path_to_images = r"C:\Users\leamon.lee\Downloads\face_mask\kaggle_dataset\images\train"
    # path_to_csv_file = path_to_images  + r'\annotations.csv'

    path_to_images = r"C:\Users\leamon.lee\Downloads\face_mask\kaggle_dataset\annotations\test"
    path_to_csv_file = r"C:\Users\leamon.lee\Downloads\face_mask\kaggle_dataset\annotations\test\annotations.csv"
    print("path_to_images:", path_to_images)
    print("path_to_csv_file:", path_to_csv_file)
    generate_csv_file(path_to_images, path_to_csv_file)
