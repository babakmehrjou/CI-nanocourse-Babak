import pytest

@pytest.fixture
def sample_data() -> list[float]:
    return [1.0, 2.0, 3.0, 4.0, 5.0]