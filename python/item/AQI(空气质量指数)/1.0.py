"""
    作者：FLY
    功能：AQI空气质量计算
    版本：1.0
    日期：05/20/2019
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
    计算单项空气质量分指数，相当于进行了范围缩放，从bp_l - bp_h 到 iaqi_l - iaqi_h
    :param iaqi_lo: 表中与bp_lo相近的空气质量分指数
    :param iaqi_hi: 表中与bp_hi相近的空气质量分指数
    :param bp_lo: 表中与cp相近的污染物浓度值的低位值
    :param bp_hi: 表中与cp相近的污染物浓度值的高位值
    :param cp: 污染物项目p的质量浓度值
    :return: 单项空气质量分指数
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    """
        计算pm2.5的IAQI
    """
    if 0<= pm_val < 35:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)

    if 36<= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)

    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)

    else:
        pass

    return iaqi


def cal_co_iaqi(co_val):
    """
        计算一氧化碳的IAQI
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)

    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)

    else:
        pass

    return iaqi


def cal_aqi(param_list):
    """
        AQI计算
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    # 分别计算pm2.5和一氧化碳的IAQI
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    return max(pm_iaqi, co_iaqi)


def main():
    """
        主函数
    """
    print('请输入以下信息，用空格分隔')
    input_str = input('(1).PM2.5 (2).CO:')
    str_list = input_str.split(' ')  # 将字符串以空格分隔
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    # 往列表中添加两个元素
    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    # 调用AQI计算函数
    aqi_val = cal_aqi(param_list)
    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
