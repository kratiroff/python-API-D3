Programming
===========

Now let's parse the response and reorganize the data so we can use it easily in the browser

Source:
```json
[
  {
    "name": "China",
    "capital": "Beijing",
    "region": "Asia",
    "subregion": "Eastern Asia",
    "population": 1377422166,
    ...
  },
  {
    "name": "Bangladesh",
    "capital": "Dhaka",
    "region": "Asia",
    "subregion": "Southern Asia",
    "population": 161006790,
    ...
  },
  {...}
]
```

Target:
```json
{
    "name": "world",
    "children": [
        {
            "name": "Asia",
            "children": [
                {
                    "name": "Eastern Asia",
                    "children": [
                        {
                            "name": "China"
                        }
                    ]
                },
                {
                    "name": "Southern Asia",
                    "children": [
                        {
                            "name": "Bangladesh"
                        }
                    ]
                },
                {...}
            ]
        },
        {...}
    ]
}
```
