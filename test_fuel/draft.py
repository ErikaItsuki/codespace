from datetime import datetime
import pytest

def validate_timestamp(timestamp):
    """Confirm that the passed in string is in the proper format %Y%m%d_%H"""
    try:
        ts = datetime.strptime(str(timestamp),'%Y%m%d_%H')
    except:
        raise ValueError("{0} must be in the format `%Y%m%d_%H".format(timestamp))
    return datetime.strftime(ts,'%Y%m%d_%H')

def test_bad_timestamp_fails():
    with pytest.raises(ValueError, match=r"foobar must be in the format `%Y%m%d_%H"):
                       validate_timestamp("foobar")
