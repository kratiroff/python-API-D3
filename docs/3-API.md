API
===

When you can click on a button, computers can use APIs.

Super umbrella term that can mean pretty much anything
    * the <select> tag you used earlier is the HTML API for a selector , i.e. the way to use it
    * a program has an API, Flask uses render_templates
    * popular subset: REST APIs
        - they manage a resource and can CRUD create read update delete
        - that's how modern dev teams work on they're own piece of code without worrying about the code of others "just send me the API docs!"
    * many businesses offer APIs, Facebook to login, google maps for uber (and a billion more examples)


Let's get a list of countries for our visualization!

Try this in your browser and in postman https://restcountries.eu/rest/v2/all

$ pip install requests

1. declar a function that fetches
2. print the result
