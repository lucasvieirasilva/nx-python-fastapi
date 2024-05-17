"""Hello unit test module."""

from lib1.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello lib1"
