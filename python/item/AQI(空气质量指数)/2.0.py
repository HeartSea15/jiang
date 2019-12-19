"""
    作者：FLY
    功能：AQI空气质量计算

    版本：2.0
    日期：05/20/2019

    JSON库：处理JSON格式的python标准库
        两个过程：
            编码encoding,将python数据类型转换成JSON格式的过程
            解码decoding，从JSON格式中解析数据对应到python数据类型的过程
        函数：
            字符串：
                dumps() ：将python数据类型转换为JSON格式字符串
                loads()：将JSON格式字符串转换为python数据类型
            文件：
                dump()：与dumps()功能一致，输出到文件
                load(): 与loads()一致，将JSON格式文件转换为python数据类型

    list.sort(func)
        fun指定了排序的方法
        func可以通过lamda函数实现

"""

import json


def process_json_file(filepath):
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
    top5_list = city_list[: 5]  # 输出前5个
    print(city_list)

    # 写入前5个
    # 写入的json文件是呈一行显示，如果让它多行显示，Google：json formatter
    f = open('top5_aqi.json', mode='w', encoding='utf-8')  # 文件名，模式，编码
    json.dump(top5_list, f, ensure_ascii=False)  # ensure_ascii=False 确保中文写入不会出现乱码
    f.close()


if __name__ == '__main__':
    main()
