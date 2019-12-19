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

    版本：:9.0
    日期：05/22/2019
"""
import pandas as pd


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

    # 基本统计
    print('AQI最大值', aqi_data['AQI'].max())
    print('AQI最小值', aqi_data['AQI'].min())
    print('AQI均值', aqi_data['AQI'].mean())

    # top10排序
    top10_citys = aqi_data.sort_values(by='AQI').head(10)
    print('空气质量最好的前10个城市')
    print(top10_citys)

    # bottom 10排序的两种方法
    bottom10_citys = aqi_data.sort_values(by='AQI', ascending=False).head(10)  # 升序为假
    # bottom10_citys = aqi_data.sort_values(by='AQI').tail(10)

    print('空气质量最差的前10个城市')
    print(bottom10_citys)

    # 保存csv文件
    top10_citys.to_csv('top10_citys', index=False) # 如果不想要索引，可以设置成False
    bottom10_citys.to_csv('bottom10_citys', index=False)


if __name__ == '__main__':
    main()
