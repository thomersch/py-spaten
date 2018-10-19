from spaten import Feature, File


def test_parse():
    with File('spaten/testfiles/polygon.spaten') as f:
        for feature in f:
            assert isinstance(feature, Feature)
