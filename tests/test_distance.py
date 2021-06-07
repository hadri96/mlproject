from mlproject.distance import haversine

def test_type_of_distance():
    assert type(haversine(0, 0, 2, 2)) == float


def test_sign_of_distance():
    assert haversine(0, 0, 2, 2) >= 0
