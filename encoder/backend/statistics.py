from typing import Dict


class EncoderStatistic:
    def __init__(self):
        self.type: str = ""
        self.calls: Dict[str, int] = {}
        self.total_calls: int = 0


def get_statistics(db):
    db.execute("SELECT * FROM calls GROUP BY type, message order by type, amount desc")
    message_groups = db.fetchall()
    statistics = []
    prev: EncoderStatistic = EncoderStatistic()

    for group in message_groups:
        if prev.type == group[0]:
            prev.calls[group[1]] = group[2]
            prev.total_calls += group[2]
        else:
            statistics.append(prev)
            prev = EncoderStatistic()
            prev.type = group[0]
            prev.calls[group[1]] = group[2]
            prev.total_calls = group[2]
    statistics.append(prev)
    statistics = statistics[1:]
    print(statistics)
    return statistics
