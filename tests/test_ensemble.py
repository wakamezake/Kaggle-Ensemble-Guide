from pathlib import Path

import pytest

from src.ensemble import Ensemble

root_path = Path("../samples")


@pytest.mark.parametrize('index_col, pred_col, glob_rule',
                         [("ImageId", "Label", "method*.csv")])
def test_ensemble(index_col, pred_col, glob_rule):
    ens = Ensemble(index_col=index_col, pred_col=pred_col, glob_rule=glob_rule)
    ens.averaging(root_path, "hoge")
