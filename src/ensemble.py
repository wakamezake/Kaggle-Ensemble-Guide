from collections import defaultdict


class Ensemble:
    def __init__(self, method="average"):
        if method != "average":
            raise ValueError
        self.scores = defaultdict(list)

    def bagging(self):
        pass

    def averaging(self):
        pass

    def rank_averaging(self):
        pass
