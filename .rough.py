                # ---------Topics to cover'---------#
#***Basic Concept of API Development using Flask***#
    # 1. Database                  - Create DB with relationships using SQlite for learning. 
    #                                   Connect to existing SQL DB or 
    #                                   Connecting to eisting MongoDB
    #                                   Establishing Multiple DB and using it.
    # 2. Marshmellow Schema        - Create schema based on input data and database. 
    #                                   JSON structure and datatypes, Serialisation and Deserialisation
    # 3. Endpoints creation        - Designing URL, HTTP methods, HTTP status codes.
    #                                   Understanding REST - https://restfulapi.net/
    # 4. Blueprints & MethodView   - Seggregate View and apply MethodViews, argument and response to endpoints
    # 5. JWT token                 - Register, Login and generate AT, Protect endpoints with access tokens,  
    #                                   Admin handling, logout handing and Token refresh handling

#***Other Required ***#
    # 6. Git commands
    # 7. Deploying as per tutorial and using Jenkins pipeline
    # 8. Documentation using POSTMAN
    # 9. Testing API using Pytest
    #10. Interview Questions

#*** Advanced concepts/Enhancements to API development***#
    #11. Image handling
    #12. Email handling
    #13. Thrid party OAuth
    #14. 







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
