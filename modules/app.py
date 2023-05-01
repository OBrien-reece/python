import converter
import ecommerce.shopping
from converter import kg_to_lbs
from ecommerce.shopping import calc_shopping
from ecommerce import shopping

from pathlib import Path
path = Path()
for file in path.glob('*.py'):
     print(file)

print(kg_to_lbs(40))
ecommerce.shopping.calc_shopping()