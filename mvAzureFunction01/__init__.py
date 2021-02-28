import logging

import azure.functions as func

# IMPORT Mark's CUSTOM python module...
from . import customFunctions as cf


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # RETRIEVE the request's queryString parameters... 
    name = req.params.get('name')
    val1 = int(req.params.get('val1'))
    val2 = int(req.params.get('val2'))

    # ADD the 2 numbers... 
    tempSum = cf.addNumbers(val1, val2)

    # LOG to the live-streaming logging engine...
    print("HEY - this message is in live-streaming logging", val1, val2, tempSum)
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. The SUM of {val1} and {val2} is {tempSum}. Marks first HTTP-triggered Azure Function executed successfully!")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
