import argparse
from pathlib import Path

import pandas as pd
from scipy.stats import ks_2samp


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("submit_file_path_1", type=str,
                         help="submission file path (csv)")
    _parser.add_argument("submit_file_path_2", type=str,
                         help="submission file path (csv)")
    _args = _parser.parse_args()
    return _args


def corr(first_file, second_file):
    first_df = pd.read_csv(first_file, index_col=0)
    second_df = pd.read_csv(second_file, index_col=0)
    # assuming first column is `prediction_id` and
    # second column is `prediction`
    prediction = first_df.columns[0]
    # correlation
    print("Finding correlation between: {} and {}".format(first_file,
                                                          second_file))
    print("Column to be measured: {}".format(prediction))
    print("Pearson's correlation score: {}".format(
        first_df[prediction].corr(second_df[prediction], method='pearson')))
    print("Kendall's correlation score: {}".format(
        first_df[prediction].corr(second_df[prediction], method='kendall')))
    print("Spearman's correlation score: {}".format(
        first_df[prediction].corr(second_df[prediction], method='spearman')))


# https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/discussion/50827
def corr_toxic(first_file, second_file):
    # assuming first column is `class_name_id`
    first_df = pd.read_csv(first_file, index_col=0)
    second_df = pd.read_csv(second_file, index_col=0)
    class_names = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult',
                   'identity_hate']

    for class_name in class_names:
        # all correlations
        print('\n Class: %s' % class_name)
        print(' Pearson\'s correlation score: %0.6f' %
              first_df[class_name].corr(
                  second_df[class_name], method='pearson'))
        print(' Kendall\'s correlation score: %0.6f' %
              first_df[class_name].corr(
                  second_df[class_name], method='kendall'))
        print(' Spearman\'s correlation score: %0.6f' %
              first_df[class_name].corr(
                  second_df[class_name], method='spearman'))
        ks_stat, p_value = ks_2samp(first_df[class_name].values,
                                    second_df[class_name].values)
        print(' Kolmogorov-Smirnov test:    KS-stat = %.6f    p-value = %.3e\n'
              % (ks_stat, p_value))


if __name__ == '__main__':
    args = get_arguments()
    first_file_path = Path(args.submit_file_path_1)
    second_file_path = Path(args.submit_file_path_2)
    if not first_file_path.exists() and not second_file_path.exists():
        raise FileExistsError("{} or {} not exists".format(first_file_path,
                                                           second_file_path))
    corr(first_file_path, second_file_path)
