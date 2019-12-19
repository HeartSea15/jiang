"""
    作者：FLY
    功能：AQI空气质量计算

        2.0：json.load(f)读json文件
            使用lamda函数对文件进行排序sort
            使用json.dump 写入排序后的json文件
        3.0：将json文件写入csv文件
        4.0： 用with打开文件，csv.reader(f)读csv文件

    版本：4.0
    日期：05/20/2019

    JSON库：处理JSON格式的python标准库
        两个过程：
            编码encoding,将python数据类型转换成JSON格式的过程
            解码decoding，从JSON格式中解析数据对应到python数据类型的过程
        函数：
            字符串：
                dumps() ：将python数据类型转换为JSON格式
                loads()：将JSON格式字符串转换为python数据类型
            文件：
                dump()：与dumps()功能一致，输出到文件
                load(): 与loads()一致，将JSON格式文件转换为python数据类型

    list.sort(func)
        fun指定了排序的方法
        func可以通过lamda函数实现
        city_list.sort(key=lambda x: x['aqi'])  # 按照元素的aqi进行从小到大排序

    json 写入：
            f = open('top5_aqi.json', mode='w', encoding='utf-8')  # 文件名，模式，编码
            json.dump(top5_list, f, ensure_ascii=False)  # ensure_ascii=False 确保中文写入不会出现乱码
            f.close()

        读入：
            f = open(filepath, mode='r', encoding='utf-8',)
            city_list = json.load(f)  # 将json格式字符串转换为python数据类型

    csv 写入：
            法1：
                f = open('aqi.csv', 'w', encoding='utf-8', newline='')  # newline=''作用是每个新行不加任何字符
                writer = csv.writer(f)
                for line in lines:
                    writer.writerow(line)
                f.close()
            法2：
                import pandas as pd
                top10_citys.to_csv('top10_citys', index=False)
        读入：
            法1：
                with open(filepath, mode='r', encoding='utf-8', newline='') as f:
                    reader = csv.reader(f)  # 将每行记录作为列表返回
                    for row in reader:
                        print(row)
                        print(','.join(row))  # 将['aqi', 'area']列表准换成整体字符串，以逗号隔开 aqi,area
            法2：
                使用pandas 读取csv文件：
                import pandas as pd
                aqi_data = pd.read_csv('china_city_aqi.csv')

"""

import json
import csv
import os


def process_json_file(filepath):
    """
        读json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)  # 将json格式字符串转换为python数据类型
    # return city_list

    # 用with的好处是不需要close文件，with模块外自动释放空间
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        读csv文件
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)  # 将每行记录作为列表返回
        for row in reader:
            # print(row)
            print(','.join(row))  # 将['aqi', 'area']列表准换成整体字符串，以逗号隔开 aqi,area


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称：')
    filname, filetxt = os.path.splitext(filepath)  # 将文件分割成文件名与扩展名

    if filetxt == '.json':
        # 处理json文件
        process_json_file(filepath)

    elif filetxt == '.csv':
        # 处理csv文件
        process_csv_file(filepath)
    else:
        print('暂不支持该文件格式！')


if __name__ == '__main__':
    main()
