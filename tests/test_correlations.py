from itertools import combinations
from pathlib import Path

import pytest

from src.correlations import corr

root_path = Path("../samples")

method_1_path = root_path / "method1.csv"
method_2_path = root_path / "method2.csv"
method_3_path = root_path / "method3.csv"


@pytest.mark.parametrize('first_path, second_path',
                         combinations([method_1_path,
                                       method_2_path,
                                       method_3_path], 2))
def test_corr(first_path, second_path):
    corr(first_path, second_path)
