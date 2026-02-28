from src.nrr import calculate_nrr


def test_nrr():

    nrr = calculate_nrr(
        200,
        20,
        180,
        20)

    assert nrr == 1.0
