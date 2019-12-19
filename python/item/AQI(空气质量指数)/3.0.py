"""
    作者：FLY
    功能：AQI空气质量计算

    版本：3.0
    日期：05/20/2019

"""

import json
import csv


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8',)
    city_list = json.load(f)  # 将json格式字符串转换为python数据类型
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')   # 如：beijing_aqi.json
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda x: x['aqi'])  # 按照元素的aqi进行从小到大排序

    lines = []
    # city_list的第一个对象的所有key放到一个list中
    a = city_list[0].keys()
    lines.append(list(city_list[0].keys()))

    for x in city_list:
        lines.append(list(x.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')  # newline=''作用是每个新行不加任何字符
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
