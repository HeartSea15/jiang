"""
    作者：FLY
    功能：AQI空气质量计算
    5.0: 通过网络链接获取网页内容，对获得的网页内容进行处理
    存在的弊端：不知道aqi是不是都是2位
              aqi_div中的空格字符串问题
    6.0：输入拼音，返回AQI，解决上述弊端
    7.0：获取所有城市
    8.0：将获取所有城市的aqi保存成csv文件，写操作
    9.0: 利用pandas进行数据处理
    10.0：数据清洗，利用pandas进行数据可视化

    版本：:10.0
    日期：05/22/2019
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    # 使用pandas 读取csv文件
    aqi_data = pd.read_csv('china_city_aqi.csv')

    print('基本信息预览：')  # object 表示字符串
    print(aqi_data.info())

    print('数据预览')
    print(aqi_data.head())  # 可以指定行数，也可以不指定
    # print(aqi_data['City'])  # 列索引
    # print(aqi_data[['City', 'AQI']])  # 不连续列索引，放在一个列表中

    # 数据清洗，保留AQI>0的数据
    condition = aqi_data['AQI']>0
    clean_data = aqi_data[condition]

    # 基本统计
    print('AQI最大值', clean_data['AQI'].max())
    print('AQI最小值', clean_data['AQI'].min())
    print('AQI均值', clean_data['AQI'].mean())

    # top10排序
    top10_citys = clean_data.sort_values(by='AQI').head(10)
    top10_citys.plot(kind='bar', x='City', y='AQI', title='空气质量最好的10个城市',
                     figsize=(20, 10))
    plt.savefig('top10_citys.png')  # 先保存，再show
    plt.show()


if __name__ == '__main__':
    main()
