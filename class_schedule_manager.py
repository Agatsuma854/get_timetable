import datetime


class class_schedule_manager():
    def __init__(self, csv_dir=''):
        self.csv_dir = csv_dir
        self.filename = ''
        self.period = 'first'

    def get_schedule(self, myclass, day_of_the_week=0, hour=0):

        try:
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
                    self.filename = (str(datetime.date.today().year) + ':' + self.period + ':' + myclass + 'csv')
                    print(self.filename)
                else:
                    self.filename = (str(datetime.date.today().year - 1) + ':' + self.period + ':' + myclass + 'csv')
                    print(self.filename)

                # CSVファイルの読み込み
        except:
            pass


# def get_free_csv_data(self,filename,day_of_the_week,hours):
#    pass

# def set_schedule_mask(self):
#    pass


if __name__ == "__main__":
    # 2019:first:1-1.csv
    while (True):
        class_schedule_manager().get_schedule("1-1")
        if input("exit:q") == 'q':
            break
