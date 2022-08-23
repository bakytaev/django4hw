from app.models import *
# b1 = Block.objects.create(number=1, cost=1100, entrances=4, floors=8, apartments_per_block=6)
b2 = Block.objects.create(number=2, cost=900, entrances=6, floors=9, apartments_per_block=8)
# b3 = Block.objects.create(number=3, cost=1500, entrances=2, floors=10, apartments_per_block=4)
o2 = Owner.objects.create(name='Paul',  purchase_date='2022-08-22', status='2', block=b2, sqmeter=70)
