'''
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,
然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。求加密后的数据
'''

def secret_num(n):
    l = []
    for i in range(4):
        ns = (int(n[i]) + 5) % 10
        l.append(ns)
    sum = l[0] + l[3]*1000 + l[1]*10 + l[2]*100
    print('加密后的数据:', sum)

if __name__ == '__main__':
    n = input('请输入要传递的数据:')
    secret_num(n)