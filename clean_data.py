"""
Purpose -
This is where you create your cleaning scripts for your data
by default this will be a transformer that returns a sklearn pipeline for cleaning data
main support for this file will be
sklearn
"""

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from load_data import load


class CleanData(BaseEstimator, TransformerMixin):
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


def c_pipe():
    """
    add standard sklearn transformed here as a part of a pip
    :return:
    """

    steps = [
        ('custom_clean', CleanData())
        # add named steps and other standard transformers here
        # ('standard scaler', StandardScaler())
    ]

    clean_pipe = Pipeline(steps=steps)

    return clean_pipe


if __name__ == "__main__":
    """
    perform clean data tests here
    """

    data = load()

    clean_pipe = c_pipe()
    clean_data = clean_pipe.transform(data)

