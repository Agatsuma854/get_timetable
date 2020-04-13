from csv import reader
from datetime import date, datetime, timedelta
import os
from typing import Dict, List, Tuple


def ext_date(l: List[int]) -> date:
    return date(l[0], l[1], l[2])


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

    def get_schedule(self, myclass: str, day_of_the_week=0) -> Dict[int, List[str]]:
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
        # 学期の初期化
        make_table = {}
        today = date.today()
        read_year = today.year if today.month >= 4 else today.year - 1
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), str(read_year) + "/limit.csv"), "r", encoding="utf-8") as f:
            rd = reader(f)
            # border[0] = [first_start.year, first_start.m, first_start.d]
            # border[1] = [second_start.y, second_start.m, second_start.d]
            border = [[int(column) for column in row] for row in rd]

            # if today >= ext_date(border[0]) and today < ext_date(border[1]):
            #     self.period = 'first'
            # elif today >= ext_date(border[1]) and today < ext_date(border[2]):
            #     self.period = 'second'
            self.period = "remote/first"

        # 読み込むファイルの名前の生成
        self.filename = (
            str(read_year)
            + '/' + self.period
            + '/' + myclass + '.csv'
        )

        # dict型に格納
        if day_of_the_week == 0:
            datemem = date.today().weekday()
            if datemem > 4:
                datemem = 0
        else:
            datemem = day_of_the_week - 1
            if datemem > 4 or datemem < 0:
                datemem = 0

        cp = self._read_csv(datemem)
        for i, data in enumerate(cp):
            make_table[i + 1] = data.split(':')

        return make_table

    # 指定したCSVファイルを読み出し
    def _read_csv(self, row_num: int) -> List[str]:
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


def day_str_converter(week="") -> Tuple[int, str]:
    """曜日または「今日」「明日」を引数として入れると
    CSVの読み出す行とその日の曜日を返す
    TODO 実装クソすぎ助けて

    Parameter
    ---------
    week : str
        検索する文字列

    Return
    ------
    tuple
        ({CSVの読み出す行番号} : int, {曜日名} : str)
    """
    weeks_ja = ["今日", "月", "火", "水", "木", "金"]

    # 引数として入れられた文字列を、weeks_jaで部分一致検索
    # 一致したものがweeks_ja配列内にあれば、weeks_jaの
    # 一致した文字列をsearch配列に入れる
    search = [s for s in weeks_ja if s in week]

    if search:
        week = search[0]
        num = (
            weeks_ja.index(week) if week != "今日"
            else date.today().weekday() + 1
        )
        try:
            return (num, weeks_ja[num])
        except IndexError:
            # 土日で「今日」を指定したとき
            return (1, "月")

    elif "明日" in week:
        num = (date.today().weekday() + 2) % 7
        if num != 0 and num != 6:
            return (num, weeks_ja[num])
        else:
            # 金土で「明日」を指定したとき
            return (1, "月")

    else:
        # 指定子と対応する要素がなかったとき

        # 時間割機能への要望「4校終了後の16:00以降は翌日の時間割を」
        # に合わせて、16時以降は翌日の時間割が配信されるように
        # 使用時間を下記に変更する
        use_time = datetime.now() + timedelta(hours=8)

        num = use_time.weekday() + 1
        try:
            return (num, weeks_ja[num])
        except IndexError:
            # 土日のとき
            return (1, "月")


if __name__ == "__main__":
    m = class_schedule_manager()
    from pprint import pprint
    pprint(m.get_schedule("AS4", 2))
    print(len(m.get_schedule("AS4", 2)))
