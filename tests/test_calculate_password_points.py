import pytest

from calculate_password_points import count_points_in_password

@pytest.mark.parametrize(
    "password,points",
    [
        ("a", 1),
        ("44", 1),
        ("4ay", 2),
        ("AAA", 2),
        ("Ab", 3),
        ("@", 3),
        ('Ab3', 4),
        ("@66", 4),
        ("@ayay", 4),
        ("B@", 5),
        ("7@a", 5),
        ("a@A", 6),
        ("7@A", 6),
        ("12345678", 6),
        ("abcabcab", 6),
        ("7@Ab", 7),
        ("abcabca8", 7),
        ("abcKbcab", 8),
        ("75cKbcab", 9),
        ("12345678!", 9),
        ("abcabcd!", 9),
        ("1bc*bcdx", 10),
        ('AAA@GFDS', 10),
        ('A88@8888', 11),
        ("abcAbcd!", 11),
        ("ExtraP@ssword!1", 12)

    ]
)
def test_count_points_in_password(password, points):
    assert count_points_in_password(password) == points