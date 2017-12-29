# -----------------------------------
# Example of rounding.
# -----------------------------------
from decimal import *

# rounding options: (ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)
def round(value, perc='.0001', option='ROUND_HALF_UP' ):
  return (Decimal(value).quantize(Decimal(perc), rounding=option))


print(round(78.909090, '.000', 'ROUND_HALF_UP'))






