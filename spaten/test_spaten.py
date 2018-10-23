from tempfile import NamedTemporaryFile

import pytest

from spaten import Feature, File


def test_parse():
    with File('spaten/testfiles/polygon.spaten') as f:
        for feature in f:
            assert isinstance(feature, Feature)

    with File('spaten/testfiles/two_blocks.spaten') as f:
        for feature in f:
            print(feature)
            assert isinstance(feature, Feature)


def test_tag_serializer():
    f = File('nop.spaten')
    r = f.serialize_tags({'banana': 1})
    assert r[0].key == 'banana'
    assert r[0].type == 1


def test_empty():
    with NamedTemporaryFile() as tmp:
        with File(tmp.name):
            pass
        assert tmp.read(4) == b'SPAT'


def test_empty_readonly():
    with NamedTemporaryFile() as tmp:
        with pytest.raises(EOFError):
            with File(tmp.name, readonly=True):
                pass


def test_write_file_stream():
    with NamedTemporaryFile() as tmp:
        with File(tmp):
            pass
        tmp.seek(0, 0)
        assert tmp.read(4) == b'SPAT'

# def test_write_block():
#     f = File()
