def whit_week(y, m, d):
    '''传入三个参数:年,月,日 返回一个周几'''
    y = y - 1 if m == 1 or m == 20 else y  # 如果月份为1月或二月返回上一年的y
    m = 13 if m == 1 else (14 if m == 2 else m)  # 如果月份为1&&2则为13&&14月,(参与运算)
    w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1  # 我也不会算,这个百度上拿到的
    return w


def math_year(y):
    '''只有一个参数,传入年份,如果是闰年返回Ture,否则False'''
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    return False


def the_math_in_day(y, m):
    """传入月份数值,返回一个当前月份的天数
    因为要判断2月的天数所以要传入年份
    """
    if m in [1, 3, 5, 7, 8, 10, 12]:  # 判断月份在不在列表中,如果在那么返回值为31天
        return 31
    elif m in [4, 6, 9, 11]:  # 返回30天的月份
        return 30
    else:
        if math_year(y):  # 这个函数是用来判断是否为闰年,如果为闰年 返回Ture,否则False
            return 29
        else:
            return 28


year = int(input('请输入年份:'))
math = int(input('请输入月份:'))

print('一   二  三  四   五   六  日')
print('*' * 25)
days = the_math_in_day(year, math)
for i in range(1, days + 1):
    v = whit_week(year, math, i)
    if i == 1:
        print(f'\t' * (v - 1), end='')  # 如果 i = 1 时判断是否为周一 如果返回周一则不添加空格
    if v == 1:  # v值为周值 如果周一时 那么输出换行符
        print()
    print(f'{i:2d}', end='\t')
