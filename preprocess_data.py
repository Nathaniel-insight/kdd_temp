"""
Purpose -
This is where you create your pre processing scripts for your data
by default this will be a transformer that returns a sklearn pipeline for pre processing data
main support for this file will be
sklearn
"""

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from load_data import load
from clean_data import c_pipe


class ProcessData(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self):
        return None

    def fit(self):
        return self

    def transform(self, X, y=None):
        """
        add basic pre processing here
        for more complex transformations see pipeline
        :param X:
        :param y:
        :return:
        """

        return X


def p_pipe():
    """
    add standard sklearn transformed here as a part of a pip
    :return:
    """

    steps = [
        ('custom_process', ProcessData())
        # add named steps and other standard transformers here
        # ('standard scaler', StandardScaler())
    ]

    process_pipe = Pipeline(steps=steps)

    return process_pipe


if __name__ == "__main__":
    """
    perform process data tests here
    """

    data = load()

    clean_pipe = c_pipe()
    clean_data = clean_pipe.transform(data)

    process_pipe = p_pipe()
    process_data = process_pipe.transform(clean_data)

