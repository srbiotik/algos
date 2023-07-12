# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
from algos import arrays


def test_tournament_winner():
    competitions = [ ["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"] ]
    results = [0, 1, 1]
    expected = "Java"
    actual = arrays.tournament_winner(competitions, results)
    assert expected == actual

def test_three_number_sum():
    data = {
        "array": [12, 3, 1, 2, -6, 5, -8, 6],
        "targetSum": 0
    }
    expected = [ [-8, 2, 6], [-8, 3, 5], [-6, 1, 5] ]
    actual = arrays.three_number_sum(data["array"], data["targetSum"])
    assert expected == actual
