import datetime

class class_schedule_manager():
    def __init__(self, csv_dir=''):
        self.csv_dir = csv_dir
        self.filename = ''
        self.period = 'first'
        self.make_table = {}

    def get_schedule(self, myclass, day_of_the_week=0):
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
            else:
                self.filename = (str(datetime.date.today().year - 1) + ':' + 'second' + ':' + myclass + '.csv')

            # dict型に格納
            if day_of_the_week == 0:
                self.datemem = datetime.date.today().weekday()
                if self.datemem > 4:
                    self.datemem = 0
            else:
                self.datemem = day_of_the_week - 1
                if self.datemem > 4 or self.datemem < 0:
                    self.datemem = 0

            cp = self._read_csv(self.datemem)
            for i, data in enumerate(cp):
                self.make_table[i + 1] = data.split(':')

        return self.make_table

    # 指定したCSVファイルを読み出し
    def _read_csv(self, row_num):
        try:
            with open(self.filename, newline='') as timetable:
                for i, list in enumerate(timetable):
                    if i == row_num:
                        return list.split(',')
            return ["Invalid date::", "Invalid date::", "Invalid date::", "Invalid date::"]
        except:
            return ["Don't read::", "Don't read::", "Don't read::", "Don't read::"]

if __name__ == "__main__":
    pass
