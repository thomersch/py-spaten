from spaten.spaten import read


def test_banana():
    with read('spaten/landmass.spaten') as f:
        for feature in f:
            print(feature)
