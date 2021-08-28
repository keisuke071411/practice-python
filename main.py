# coding:utf-8
num = 1

num2 = 5

total_num = num + num2

hackz_member_list = ['take', 'yuto', 'keisuke', 'meguru', 'miki', 'issei']


# クラスの定義
class hackz_members:
    def __init__(self, name, cup):
        self.name = name
        self.cup = cup

    def produce(self):
        print('{}のお{}は{}カップ'.format(self.name, 'python', self.cup))


# if文使ってみた
if total_num == 6:
    print('success!!')


# for文使ってみた
for hackz_member in hackz_member_list[0:3]:
    print(hackz_member)


# 関数使ってみた
def python_sample():
    for hackz_member in hackz_member_list[0:total_num]:
        print('{}のお{}は{}カップ'.format(hackz_member, 'python', 'B'))

python_sample()


# インスタンスの生成
take = hackz_members('take', 'A')
yuto = hackz_members('yuto', 'B')
keisuke = hackz_members('keisuke', 'C')
meguru = hackz_members('meguru', 'D')
miki = hackz_members('miki', 'E')
issei = hackz_members('issei', 'F')


# メソッドの呼び出し
take.produce()
yuto.produce()
keisuke.produce()
meguru.produce()
miki.produce()
issei.produce()

