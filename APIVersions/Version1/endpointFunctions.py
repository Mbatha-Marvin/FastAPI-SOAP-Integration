from Lib.ZeepSoapClient.SoapMethods import CheckOrderStatus, SubmitPurchaseOrder
from Lib.ZeepSoapClient.SoapTypes import (
    ArrayOfPurchaseOrderDetailLineType,
    FulfillmentMethodType,
    PaymentMethodType,
    ShipViaType,
)
from Lib.LocalExcelClient.Operations import (
    getAllRecords,
    getCustomerNameContact,
    getCustomerData,
    getSkuList,
    getPurchaseOrderNumber,
    getCustomerAdresses,
    getDetailLineArray,
)
from APIVersions.Version1.Models.RequestBody import (
    CheckOrderStatusRequestBody,
    SubmitPurchaseOrderRequestBody,
)


def EndpointCheckOrderStatus(
    requestBody: CheckOrderStatusRequestBody,
):
    DealerAccountNumber = str(requestBody.DealerAccountNumber)
    OrderConfirmationNumber = str(requestBody.OrderConfirmationNumber)
    Password = str(requestBody.Password)
    UserId = str(requestBody.UserId)

    if (OrderConfirmationNumber == None) | (OrderConfirmationNumber == ""):
        PurchaseOrderDetails = getPurchaseOrderNumber()
        # OrderConfirmationNumber = "4147395"
        OrderConfirmationNumber = PurchaseOrderDetails["PurchaseOrderNumber"]

    response = CheckOrderStatus(
        DealerAccountNumber=DealerAccountNumber,
        OrderConfirmationNumber=OrderConfirmationNumber,
        Password=Password,
        UserId=UserId,
    )

    return response


def EndPointSubmitPurchaseOrder(requestBody: SubmitPurchaseOrderRequestBody):
    BypassAddressValidation = requestBody.BypassAddressValidation
    ConfirmToEmailAddress = requestBody.ConfirmToEmailAddress
    ConfirmToName = requestBody.ConfirmToName
    CreditCardCV2 = requestBody.CreditCardCV2
    DealerAccountNumber = requestBody.DealerAccountNumber
    DetailLines = requestBody.DetailLines
    ExternalPO = requestBody.ExternalPO
    FulfillmentMethod = requestBody.FulfillmentMethod
    IsDropShip = requestBody.IsDropShip
    KrollVaultCreditCardDescription = requestBody.KrollVaultCreditCardDescription
    Password = requestBody.Password
    PaymentMethod = requestBody.PaymentMethod
    PurchaseOrderNumber = requestBody.PurchaseOrderNumber
    ShipToAddress1 = requestBody.ShipToAddress1
    ShipToAddress2 = requestBody.ShipToAddress2
    ShipToAddress3 = requestBody.ShipToAddress3
    ShipToCity = requestBody.ShipToCity
    ShipToCountryCode = requestBody.ShipToCountryCode
    ShipToName = requestBody.ShipToName
    ShipToPostalCode = requestBody.ShipToPostalCode
    ShipToStateProvince = requestBody.ShipToStateProvince
    ShipToTelephoneNumber = requestBody.ShipToTelephoneNumber
    ShipVia = requestBody.ShipVia
    SignatureRequired = requestBody.SignatureRequired
    UserId = requestBody.UserId

    addresses = getCustomerAdresses()
    ShipToAddress1 = addresses["address1"]
    ShipToAddress2 = addresses["address2"]
    ShipToCity = addresses["city"]
    ShipToStateProvince = addresses["state"]
    zipcode = addresses["zipcode"]
    ShipToCountryCode = "USA"
    FulfillmentMethod = FulfillmentMethodType(
        "ShipProductThatIsAvailableNowAndOtherProductWhenAvailable"
    )
    PaymentMethod = PaymentMethodType("AccountTerms")
    ShipVia = ShipViaType("FlatRate")

    response = SubmitPurchaseOrder(
        BypassAddressValidation=BypassAddressValidation,
        ConfirmToEmailAddress=ConfirmToEmailAddress,
        ConfirmToName=ConfirmToName,
        CreditCardCV2=CreditCardCV2,
        DealerAccountNumber=DealerAccountNumber,
        DetailLines=DetailLines,
        ExternalPO=ExternalPO,
        FulfillmentMethod=FulfillmentMethod,
        IsDropShip=IsDropShip,
        KrollVaultCreditCardDescription=KrollVaultCreditCardDescription,
        Password=Password,
        PaymentMethod=PaymentMethod,
        PurchaseOrderNumber=PurchaseOrderNumber,
        ShipToAddress1=ShipToAddress1,
        ShipToAddress2=ShipToAddress2,
        ShipToAddress3=ShipToAddress3,
        ShipToCity=ShipToCity,
        ShipToCountryCode=ShipToCountryCode,
        ShipToName=ShipToName,
        ShipToPostalCode=ShipToPostalCode,
        ShipToStateProvince=ShipToStateProvince,
        ShipToTelephoneNumber=ShipToTelephoneNumber,
        ShipVia=ShipVia,
        SignatureRequired=SignatureRequired,
        UserId=UserId,
    )

    return response
