

"""
stores = {
    'f0c1874f96094dc99b3be3ea19da91c4': {
        'name': 'My Store 2', 
        'id': 'f0c1874f96094dc99b3be3ea19da91c4'}
        }

items = {
    "c95a3cdeaae24dd0b18f762f5f4e9790": {
        "item": "Chair",
        "price": 159.35,
        "store_id": "e56042d2891f40cba0253be68eddca52"
    }
}

print(stores.values())
print(list(stores.values()))
if "f0c1874f96094dc99b3be3ea19da91c4" in stores:
    print("Exists")
del stores["f0c1874f96094dc99b3be3ea19da91c4"]
print(stores)
 """


policy = {
    "ProductName"       : "Life click 1D", 
    "PolicyHolder"      : "Aditya",
    "LifeInsured"       : "Aditya",
    "Nominee"           : "Kavya",
    "PremiumAmount"     :  13715.00,
    "CoverageStartDate" : "01-03-2023",
    "CoverageEndDate"   : "01-03-2063",
    "FundIndicator"     : True}

print(policy)
