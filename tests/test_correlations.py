from itertools import combinations
from pathlib import Path

import pytest

from src.correlations import corr, corr_toxic

root_path = Path("../samples")
toxic_path = root_path / "ToxicCommentClassificationChallenge"

method_1_path = root_path / "method1.csv"
method_2_path = root_path / "method2.csv"
method_3_path = root_path / "method3.csv"

model_1_path = toxic_path / "Logistic_regression_with_words_and" \
                            "_char_n-grams.csv"
model_2_path = toxic_path / "NB_SVM_strong_linear_baseline.csv"
model_3_path = toxic_path / "pooled-gru-fasttext.csv"


@pytest.mark.parametrize('first_path, second_path',
                         combinations([method_1_path,
                                       method_2_path,
                                       method_3_path], 2))
def test_corr(first_path, second_path):
    corr(first_path, second_path)


@pytest.mark.parametrize('first_path, second_path',
                         combinations([model_1_path,
                                       model_2_path,
                                       model_3_path], 2))
def test_corr_toxic(first_path, second_path):
    corr_toxic(first_path, second_path)
