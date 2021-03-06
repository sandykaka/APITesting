# APITesting

###### This repo includes API testing architecture. This is using following technologies:
1. Behave   (BDD framework for python)
2. Python
3. Requests (lib for making api calls)
4. json
5. pymongo (for db connection)

## How to setup the Project:
1. Clone the repo
2. Go ot APITesting
3. Run command => ```pip install requirments.txt```


## How to run the feaure file:
Inside the APITesting directory run this command ```behave features/access_application.feature```

## Project Structure:
```
.
├── README.md
├── data
│   └── create_application_input_data.json
├── features
│   ├── eFormsAPI_Create.feature
│   ├── eFormsAPI_Update.feature
│   ├── eformsAPI_request_application_pdf.feature
│   └── steps
│       └── eformapi_impl.py
├── libs
│   ├── __init__.py
│   ├── access_database.py
│   ├── api_requests.py
│   └── logging.py
├── lra
│   ├── __init__.py
│   └── ira_app.py
└── requirements.txt
```
### Brief Information:
1. libs => liberary like connection to db, request to make to api and logging liberary
2. ira => core methods to make api call related to application
3. features => feature files
4. features/steps => All the bindings for feature files
5. data => json data
