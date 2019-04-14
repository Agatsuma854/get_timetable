import datetime


class class_schedule_manager():
    def __init__(self, csv_dir=''):
        self.csv_dir = csv_dir
        self.filename = ''
        self.period = 'first'
        self.return_value = {}

    def get_schedule(self, myclass, day_of_the_week=0):

        # try:
        # config.csvファイルの読み込み
        with open('config.csv', newline='') as config:

            # 学期の初期化
            self.period = 'first'

            for line in config:
                # 学期の判定と決定
                if (datetime.date.today().year == int(line[0]) and datetime.date.today().month <= int(line[
                                                                                                          1]) and datetime.date.today().day <= int(
                    line[2])):
                    self.period = 'second'

            # 読み込むファイルの名前の生成
            if datetime.date.today().month >= 4:
                self.filename = (str(datetime.date.today().year) + ':' + self.period + ':' + myclass + '.csv')
                print(self.filename)
            else:
                self.filename = (str(datetime.date.today().year - 1) + ':' + 'second' + ':' + myclass + '.csv')
                print(self.filename)

            # CSVファイルの読み込み
            with open(self.filename, newline='') as timetable:
                self.rawcsv = []
                for i, list in enumerate(timetable):
                    self.rawcsv.append(list)

                print(self.rawcsv)

                # dict型に格納
                if day_of_the_week == 0:
                    pass
                elif day_of_the_week == 6:
                    pass
                else:
                    pass

    # except:
    # print("tin")

    def read_csv(self, csv_obj, row_num):
        for i, list in enumerate(csv_obj):
            if i == row_num:
                return list.split(',')
        return []


# 行を指定し

# 行出して(曜日で分解) a:b:c:,d:e:f,g:h:i,j:k:l  extract_csv(timetable,num) : return [a:b:c,d]
# それを時間ごとに[i]にして a:b:c
# テキスト内の:を目印に[きょうか,ひと,場所]にわける [a,b,c] extract_str(str,num) <- str[i] で渡す
# これを{}に格納 { 1:[a,b,c]} 返り値で実装

# def get_free_csv_data(self,filename,day_of_the_week,hours):
#    pass

# def set_schedule_mask(self):
#    pass


if __name__ == "__main__":
    # 2019:first:1-1.csv
    # class_schedule_manager().get_schedule(1-1)
    with open("2019:first:1-1.csv", newline='') as timetable:
        rawcsv = []
        print(timetable)
        for i, list in enumerate(timetable):
            list = list.split(',')
            print(list[1])
