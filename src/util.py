import argparse


def get_arguments():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("submit_file_path_1", type=str,
                         help="submission file path (csv)")
    _parser.add_argument("submit_file_path_2", type=str,
                         help="submission file path (csv)")
    _args = _parser.parse_args()
    return _args
