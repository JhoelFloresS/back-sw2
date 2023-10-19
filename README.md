# API RECOMMENDATION

The api:

/api/similary with query parameters store=<store_id>

e.g.
```
 /api/similary?store=10001
```

return a json like:

```javascript

    [
        similitud {
            <name_store>: <similitud[0-1]>
            ...
        }
        productos: {
            0: <producto_a>
            1: <producto_b>
            ...
        }
    ]

```

The similarity object has the store names as an index and the similarity index as a value.

The product object has all the recommended products based on the most similar store



# To start
1. create the .env file from .env.example
2. Activate the environment
```
    .venv\Scripst\activate
```
3. Install packages
```
    py -m pip install -r requirements.txt
```
4. start
```
    py app.py
```