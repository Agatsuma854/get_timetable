from datetime import date

import os


class class_schedule_manager():
    """指定したクラスの時間割を取得します

    Examples
    --------
    >>> l = ["1-1", "火"]
    >>> m = class_schedule_manager()
    >>> weekday = m.day_str_converter(l[1])
    >>> m.get_schedule(l[0], weekday)
    {1: ['地理', '矢澤', '教室'], 2: ['総合工学基礎', ], }
    """
    def __init__(self, csv_dir=''):
        self.csv_dir = csv_dir
        self.filename = ''
        self.period = 'first'
        self.make_table = {}

    def get_schedule(self, myclass : str, day_of_the_week=0):
        """ファイルの読み込みをし、使用しやすいような形式にした
        ものを返す
        Parameters
        ----------
        myclass : str
            1学年は `1-1` 表記
            上位学年は `IS3` など半角大文字で

        day_of_the_week : int
            0...今日分
            引数指定がなければ本日分を返します
            その他の曜日指定は datetime.date.weekday() +1
            範囲: 0~5

        Return
        ------
        dict
            {1: ['地理', '矢澤', '教室'], 2: ['総合工学基礎', ...], ...}
            など
        """
        # config.csvファイルの読み込み
        with open(os.path.join(os.path.abspath(
                os.path.dirname(__file__)), 'config.csv'),
                newline='', encoding="utf-8") as config:

            # 学期の初期化
            self.period = 'first'

            for line in config:
                # 学期の判定と決定
                if (date.today().year == int(line[0])
                        and date.today().month <= int(line[1])
                        and date.today().day <= int(line[2])):
                    self.period = 'second'

            # 読み込むファイルの名前の生成
            if date.today().month >= 4:
                self.filename = (
                    str(date.today().year)
                    + '_' + self.period
                    + '_' + myclass + '.csv'
                )
                print(self.filename)
            else:
                self.filename = (
                    str(date.today().year - 1)
                    + '_' + 'second'
                    + '_' + myclass + '.csv'
                )
                print(self.filename)

            # dict型に格納
            if day_of_the_week == 0:
                self.datemem = date.today().weekday()
                if self.datemem > 4:
                    self.datemem = 0
            else:
                self.datemem = day_of_the_week - 1

            cp = self._read_csv(self.datemem)
            for i, data in enumerate(cp):
                self.make_table[i + 1] = data.split(':')

        return self.make_table

    # 指定したCSVファイルを読み出し
    def _read_csv(self, row_num : int):
        """
        Parameter
        ---------
        row_num : int
            csvファイルの行が曜日を示しているので、
            引数で行の数を指定することで曜日を示す
            1: 月、 2: 火, ...

        Return
        ------
        list
            ['地理', '矢澤', '教室'] など
            ファイルのコンマで要素を分けてリスト化したものを返す
        """
        with open(os.path.join(os.path.abspath(
                os.path.dirname(__file__)), self.filename), 
                newline='', encoding="utf-8") as timetable:
            for i, row in enumerate(timetable):
                if i == row_num:
                    row = row.strip()
                    # ここのでーたの状態 [e:b:c, ]
                    return row.split(',')
        return [
            "Invalid date::", "Invalid date::",
            "Invalid date::", "Invalid date::"
        ]


    def day_str_converter(self, week : str):
        weeks_ja = ["今日", "月", "火", "水", "木", "金"]
        if week in weeks_ja:
            num = (
                weeks_ja.index(week) if week != "今日"
                else date.today().weekday() + 1
            )
            try:
                return (num, weeks_ja[num])
            except IndexError:
                return (0, "月")
        elif "明日" in week:
            num = (date.today().weekday() + 2) % 7
            try:
                return (num, weeks_ja[num])
            except IndexError:
                return (0, "月")
        else:
            return (0, "月")


# 行を指定し

# 行出して(曜日で分解) a:b:c:,d:e:f,g:h:i,j:k:l  extract_csv(timetable,num) : return [a:b:c,d]
# それを時間ごとに[i]にして a:b:c
# テキスト内の:を目印に[きょうか,ひとte,場所]にわける [a,b,c] extract_str(str,num) <- str[i] で渡す
# これを{}に格納 { 1:[a,b,c]} 返り値で実装

# def get_free_csv_data(self,filename,day_of_the_week,hours):
#    pass

# def set_schedule_mask(self):
#    pass


if __name__ == "__main__":
    # 2019:first:1-1.csv
    obj = class_schedule_manager()
    print(obj.get_schedule("1-1"))
