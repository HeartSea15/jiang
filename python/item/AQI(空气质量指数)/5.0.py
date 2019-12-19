"""
    作者：FLY
    功能：AQI空气质量计算
    5.0: 通过网络链接获取网页内容，对获得的网页内容进行处理
    版本：5.0
    日期：05/21/2019
"""
import requests


def get_html_txt(url):
    """
        返回url文本
    """
    r = requests.get(url)  # 网页请求
    print(r.status_code)   # HTTP的返回状态，200成功，400失败
    return r.text          # 返回HTTP的页面内容，字符串形式


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_txt = get_html_txt(url)

    # 获取59所在的div子字符串
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''  # 注意前面是有空格字符串的

    # 找到子字符串在整体字符串的位置 find
    index = url_txt.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2  # 2是两个数字的长度
    aqi_value = url_txt[begin_index:end_index]
    print('空气质量输出：{}'.format(aqi_value))


if __name__ == '__main__':
    main()
