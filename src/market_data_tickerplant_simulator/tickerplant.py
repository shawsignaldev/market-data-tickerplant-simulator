from dataclasses import dataclass

@dataclass(frozen=True)
class QuoteUpdate:
    side: str
    price: float
    size: int

def top_of_book(updates: list[QuoteUpdate]) -> dict[str, tuple[float, int] | None]:
    bids = [(u.price, u.size) for u in updates if u.side == "bid" and u.size > 0]
    asks = [(u.price, u.size) for u in updates if u.side == "ask" and u.size > 0]
    return {
        "bid": max(bids, default=None),
        "ask": min(asks, default=None),
    }
