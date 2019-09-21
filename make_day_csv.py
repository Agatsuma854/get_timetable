from csv import reader as rd
from csv import writer as wr

classes = (
    "1-1", "1-2", "1-3", "IS2", "IT2", "IE2",
    "IS3", "IT3", "IE3", "IE4", "IS4", "IN4",
    "IE5", "IS5", "IN5"
)


def make_csv(dir_path: str):
    data = {
        "mon": [[], [], [], []],
        "tue": [[], [], [], []],
        "wed": [[], [], [], []],
        "thu": [[], [], [], []],
        "fri": [[], [], [], []]
    }
    for c in classes:
        with open("%s/%s.csv" % (dir_path, c), "r", newline="", encoding="utf-8") as f:
            reader = rd(f)
            # 曜日ループ
            for day, row in zip(data, reader):
                # 時間(行)ループ
                for i, jkdata in enumerate(row):
                    data[day][i].append("%s:%s" % (c, jkdata))

    print(data)
    input("ok?: ")

    for day, jkdata in data.items():
        with open("%s/date/%s.csv" % (dir_path, day), "w", newline="", encoding="utf-8") as f:
            writer = wr(f)
            writer.writerows(jkdata)

if __name__ == "__main__":
    path = input("where?: ")
    make_csv(path)
