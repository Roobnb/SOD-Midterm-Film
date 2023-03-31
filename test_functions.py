# test if it can return the right rating for a movie with known rating
def test_valid_url_with_known_rating(url):
    url = "https://en.wikipedia.org/wiki/Moonlight_(2016_film)"
    expected_rating = "9.00/10"
    assert get_movie_rating(url) == expected_rating




# Test for an invalid url
def test_invalid_url(url):
    url = "https://en.wikipedia.org/wiki/HTTP_404"
    expected_rating = None
    assert get_movie_rating(url) == expected_rating




# Test for a known movie with budget known
def test_url_with_known_budget(url):
    url = "https://en.wikipedia.org/wiki/Iron_Man_(2008_film)"
    expected_budget = "140"
    assert get_movie_budgets(url) == expected_budget




# Test for a movie with a range of budget shown




def test_url_with_range_budgets(url):
    url = "https://en.wikipedia.org/wiki/Justice_League_(film)"
    expected_budget = "300"
    assert get_movie_budgets(url) == expected_budget




# For this, if it is shown a range of budget, we will get the first number as expected budget




# Test if it can return the right year for a movie with known published date
def test_valid_url_with_known_year(url):
    url = "https://en.wikipedia.org/wiki/Iron_Man_3"
    expected_year = 2013
    assert get_movie_year(url) == expected_year




# test for an invalid url




def test_invalid_url(url):
    url = "https://en.wikipedia.org/wiki/never.appeared.before"
    expected_year = None
    assert get_movie_year(url) == expected_year