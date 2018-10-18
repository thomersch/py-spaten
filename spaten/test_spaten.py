from spaten.spaten import read


def test_parse():
    with read('spaten/testfiles/point2.spaten') as f:
        for feature in f:
            print(feature)
