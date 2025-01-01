from pandas import DataFrame, Series


def predict_scores(student_input: DataFrame) -> Series:
    return Series([50] * len(student_input), name='average_score')
