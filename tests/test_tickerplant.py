from market_data_tickerplant_simulator.tickerplant import QuoteUpdate, top_of_book

def test_top_of_book_tracks_best_bid_and_ask() -> None:
    updates = [QuoteUpdate("bid", 100.0, 10), QuoteUpdate("bid", 100.2, 5), QuoteUpdate("ask", 100.5, 8)]
    assert top_of_book(updates) == {"bid": (100.2, 5), "ask": (100.5, 8)}

def test_top_of_book_ignores_empty_side() -> None:
    assert top_of_book([QuoteUpdate("bid", 10.0, 1)]) == {"bid": (10.0, 1), "ask": None}
