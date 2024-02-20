from flask import Flask

app=Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            },
            {
                "name": "Table",
                "price": 19.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}