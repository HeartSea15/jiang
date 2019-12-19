"""
    作者：FLY
    功能：AQI空气质量计算
    5.0: 通过网络链接获取网页内容，对获得的网页内容进行处理
    存在的弊端：不知道aqi是不是都是2位
              aqi_div中的空格字符串问题
    6.0：输入拼音，返回AQI，解决上述弊端
    版本：:6.0
    日期：05/21/2019
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)  # 等待30秒，30秒无结果就不等了
    bs = BeautifulSoup(r.text, 'lxml')  # 创建BeautifulSoup对象，页面内容，指定解码器
    div_list = bs.find_all('div', {'class': 'span1'})  # 找到左右的div节点，指定条件：class = span1

    city_aqi = []
    for i in range(8):
        city_content = div_list[i]
        a = city_content.find('div', {'class': 'caption'})
        b = a.text
        caption = city_content.find('div', {'class': 'caption'}).text.strip()  # 获取节点内的内容，strip()移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        value = city_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))

    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)

    print('空气质量输出：{}'.format(city_aqi))


if __name__ == '__main__':
    main()
