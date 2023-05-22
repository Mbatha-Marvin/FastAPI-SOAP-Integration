from fastapi import FastAPI
from fastapi_versioning import version, VersionedFastAPI
from APIVersions.Version1.Models.RequestBody import (
    CheckOrderStatusRequestBody,
    SubmitPurchaseOrderRequestBody,
)
from APIVersions.Version1.endpointFunctions import EndpointCheckOrderStatus, EndPointSubmitPurchaseOrder
from Lib.ZeepSoapClient.SoapMethods import CheckOrderStatus

app = FastAPI(title="Soap Integration")

@app.get("/")
@version(1)
def homePage():
    return {"Message" : "Welcome to the Soap Integration API"}

@app.post("/checkOrderStatus")
@version(1)
def checkOrderStatus(requestBody: CheckOrderStatusRequestBody):    
    
    response = EndpointCheckOrderStatus(requestBody=requestBody)
    
    return response

@app.post("/submitPurchaseOrder")
@version(1)
def submitPurchaseOrder(requestBody : SubmitPurchaseOrderRequestBody):
    
    print(requestBody)
    
    response = EndPointSubmitPurchaseOrder(requestBody=requestBody)
    
    
    return response


app = VersionedFastAPI(app, version_format="{major}", prefix_format="/v{major}")
