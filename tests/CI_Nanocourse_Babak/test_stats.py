import pytest
from CI_Nanocourse_Babak.stats import mean

def test_mean_happy_path(sample_data):
    print(sample_data)
    assert mean(sample_data) == 3.0

def test_mean_empty_raises(sample_data):
    with pytest.raises(ValueError):
        mean([])