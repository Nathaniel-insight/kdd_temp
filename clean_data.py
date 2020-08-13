"""
Purpose -
This is where you create your cleaning scripts for your data
by default this will be a transformer that returns a sklearn pipeline for cleaning data
main support for this file will be
sklearn
"""

from sklearn.base import BaseEstimator, TransformerMixin
from load_data import load


class clean_data(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self):
        return None

    def fit(self):
        return self

    def transform(self, X, y=None):
        """
        add basic transformations here
        for more complex transformations see pipeline
        :param X:
        :param y:
        :return:
        """

        return X

def clean_pipe():
    """
    add standard sklearn transformed here as a part of a pip
    :return:
    """


if __name__ == "__main__":
    """
    perform clean data tests here
    """

    data = load()