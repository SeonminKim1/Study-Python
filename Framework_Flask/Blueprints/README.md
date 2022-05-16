### Structure
```
├── routers
│   ├── router_1.py // money
│   └── router_2.py // greet
└── app.py          // 진입점
``` 

### API Endpoint
- @router1.route("/earn")  => money/earn
- @router1.route("/lose")  => money/lose 
- @router2.route("/hi")    => greet/hi
- @router2.route("/hello") => greet/hello
