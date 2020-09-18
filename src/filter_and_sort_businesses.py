# <-- EXPAND to see the data classes
import json
import sys
from typing import List
from typing import NamedTuple
from typing import Optional


class Business(NamedTuple):
    id: int
    rating: float
    vegan_friendly: bool
    price: int
    distance: float

"""
Example:

Input:
    businesses: [
        Business(id=1, rating=4.0, vegan_friendly=True, price=4, distance=10.0),
        Business(id=2, rating=2.5, vegan_friendly=False, price=2, distance=5.0),
        Business(id=3, rating=4.5, vegan_friendly=False, price=1, distance=1.0),
        Business(id=4, rating=3.0, vegan_friendly=True, price=2, distance=3.4),
        Business(id=5, rating=4.5, vegan_friendly=true, price=1, distance=6.3),
        Business(id=6, rating=3.5, vegan_friendly=True, price=2, distance=1.2),
    ]
    only_vegan_friendly: False
    max_price: None
    max_distance: 6.0

Output:
    [3, 6, 4, 2]
"""


def filter_and_sort_businesses(
    businesses: List[Business],
    only_vegan_friendly: bool = False,
    max_price: Optional[int] = None,
    max_distance: Optional[float] = None,
) -> List[int]:
    return []

def main():
    input_json = json.load(sys.stdin)
    businesses = [
        Business(
            id=business['id'],
            rating=business['rating'],
            vegan_friendly=business['vegan_friendly'],
            price=business['price'],
            distance=business['distance'],
        )
        for business in input_json['businesses']
    ]
    businesses_out = filter_and_sort_businesses(
        businesses=businesses,
        only_vegan_friendly=input_json['filters']['only_vegan_friendly'],
        max_price=input_json['filters'].get('max_price', None),
        max_distance=input_json['filters'].get('max_distance', None),
    )

    for business_id in businesses_out:
        print(business_id)


if __name__ == '__main__':
    main()