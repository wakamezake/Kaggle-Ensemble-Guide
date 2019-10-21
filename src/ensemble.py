from collections import defaultdict
from pathlib import Path

import pandas as pd


class Ensemble:
    def __init__(self, index_col, pred_col, glob_rule="*", method="average"):
        if method != "average":
            raise ValueError
        self.scores = defaultdict(list)
        self.index_col = index_col
        self.pred_col = pred_col
        self.glob_rule = glob_rule

    def bagging(self):
        pass

    def averaging(self, input_path: Path, output_path: Path):
        scores = None
        start_idx = 1
        for idx, csv_path in enumerate(input_path.glob(self.glob_rule),
                                       start_idx):
            print("parsing: {}".format(csv_path))
            df = pd.read_csv(csv_path).sort_values(by=self.index_col)
            prediction = df[self.pred_col]
            if idx == start_idx:
                scores = prediction
            else:
                scores += prediction
        df[self.pred_col] = scores / idx
        print(df)

    def rank_averaging(self, input_path, output_path):
        pass
