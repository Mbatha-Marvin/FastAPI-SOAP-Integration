from zeep import Client
from typing import Optional


def CheckOrderStatus(
    DealerAccountNumber: str | None = None,
    OrderConfirmationNumber: str | None = None,
    Password: str | None = None,
    UserId: str | None = None,
) -> dict:
    if (OrderConfirmationNumber == None) | (OrderConfirmationNumber == ""):
        return "OrderConfirmationNumber Must Be Provided !!!"

    if (DealerAccountNumber == None) | (DealerAccountNumber == ""):
        DealerAccountNumber = "18882"
    if (Password == None)| (Password == ""):
        Password = "48e000f8bf98457caa78bfcc0b14d3e8"

    if (UserId == None) | (UserId == ""):
        UserId = "purchasing@ecoppolicesupply.com"

    client = Client(
        wsdl="https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl"
    )
    CheckOrderStatusRequestType = client.get_type("ns2:CheckOrderStatusRequest")
    CheckOrderStatusRequestElement = CheckOrderStatusRequestType(
        DealerAccountNumber, OrderConfirmationNumber, Password, UserId
    )

    return client.service.CheckOrderStatus(CheckOrderStatusRequestElement)


def SubmitPurchaseOrder(
    FulfillmentMethod: dict | str = "",
    IsDropShip: bool | str = "",
    PaymentMethod: dict | str = "",
    ShipVia: dict | str = "",
    
    BypassAddressValidation :str="",
    ConfirmToEmailAddress :str="",
    ConfirmToName :str="",
    CreditCardCV2 :str="",
    DealerAccountNumber :str="",
    DetailLines:str ="",
    ExternalPO :str="",
    KrollVaultCreditCardDescription :str="",
    Password :str="",
    PurchaseOrderNumber :str="",
    ShipToAddress1 :str="",
    ShipToAddress2 :str="",
    ShipToAddress3 :str="",
    ShipToCity :str="",
    ShipToCountryCode :str="",
    ShipToName :str="",
    ShipToPostalCode :str="",
    ShipToStateProvince :str="",
    ShipToTelephoneNumber :str="",

    SignatureRequired :str="",
    UserId :str="",
) -> dict:
    if (DealerAccountNumber == None) | (DealerAccountNumber == ""):
        DealerAccountNumber = "18882"
    if (Password == None) | (Password == ""):
        Password = "48e000f8bf98457caa78bfcc0b14d3e8"
    if (UserId == None) | (UserId == ""):
        UserId = "purchasing@ecoppolicesupply.com"

    cumpulsoryFieldsList = [FulfillmentMethod, IsDropShip, PaymentMethod, ShipVia]

    if all(field != "" for field in cumpulsoryFieldsList):
        # print("Empty string test Test Passed")
        pass
    else:
        return "Empty string detected, Provide all values for Compulsory fields"

    if all(field is not None for field in cumpulsoryFieldsList):
        # print("Not None Test Passed")
        pass
    else:
        return "None/Null value detected, Provide all values for Compulsory fields"

    client = Client(
        wsdl="https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl"
    )
    PurchaseOrderRequestType = client.get_type("ns2:PurchaseOrderRequest")

    PurchaseOrderRequestElement = PurchaseOrderRequestType(
        BypassAddressValidation,
        ConfirmToEmailAddress,
        ConfirmToName,
        CreditCardCV2,
        DealerAccountNumber,
        DetailLines,
        ExternalPO,
        FulfillmentMethod,
        IsDropShip,
        KrollVaultCreditCardDescription,
        Password,
        PaymentMethod,
        PurchaseOrderNumber,
        ShipToAddress1,
        ShipToAddress2,
        ShipToAddress3,
        ShipToCity,
        ShipToCountryCode,
        ShipToName,
        ShipToPostalCode,
        ShipToStateProvince,
        ShipToTelephoneNumber,
        ShipVia,
        SignatureRequired,
        UserId,
    )

    return client.service.SubmitPurchaseOrder(PurchaseOrderRequestElement)


# def SubmitCreditCardPurchaseOrder (
#         BypassAddressValidation: bool | None = None,
#         ConfirmToEmailAddress: str = None,
#         ConfirmToName: str = None,
#         CreditCardCV2: Optional[str] = None,
#         DealerAccountNumber: str = None,
#         DetailLines: dict | None = None,
#         ExternalPO: str = None,
#         FulfillmentMethod: dict | None = None,
#         IsDropShip: bool | None = None,
#         KrollVaultCreditCardDescription: Optional[str]= None,
#         Password: str = None,
#         PaymentMethod: dict | None = None,
#         PurchaseOrderNumber: str = None,
#         ShipToAddress1: str = None,
#         ShipToAddress2: Optional[str] = None,
#         ShipToAddress3: Optional[str] = None,
#         ShipToCity: str = None,
#         ShipToCountryCode: str = None,
#         ShipToName: str = None,
#         ShipToPostalCode: str = None,
#         ShipToStateProvince: str = None,
#         ShipToTelephoneNumber: Optional[str] = None,
#         ShipVia: dict | None = None,
#         SignatureRequired: bool | None = None,
#         UserId: str = None,
#         BillingCardAddress1: str = None,
#         BillingCardCity: str = None,
#         BillingCardCountryCode: str = None,
#         BillingCardPostalCode: str = None,
#         BillingCardStateProvince: str = None,
#         CreditCardNumber: str = None,
#         ExpirationMonth: str = None,
#         ExpirationYear: str = None,
#         SaveForFutureUse: bool | None = None
#         ) -> dict:
#     #  Assign default values for account details
#     if DealerAccountNumber == None:
#         DealerAccountNumber = "18882"
#     if Password == None:
#         Password = "48e000f8bf98457caa78bfcc0b14d3e8"
#     if UserId == None:
#         UserId = "purchasing@ecoppolicesupply.com"

#     # Assign Empty string to optional fields if None is provided
#     if CreditCardCV2 == None:
#         CreditCardCV2 = ""
#     if KrollVaultCreditCardDescription == None:
#         KrollVaultCreditCardDescription = ""
#     if ShipToAddress2 == None:
#         ShipToAddress2 = ""
#     if ShipToAddress3 == None:
#         ShipToAddress3 = ""
#     if ShipToTelephoneNumber == None:
#         ShipToTelephoneNumber = ""

#     # Dictionary of compulsory fields to check if values are provided
#     compulsoryFieldsList = [
#         BypassAddressValidation,ConfirmToEmailAddress, ConfirmToName, DealerAccountNumber, DetailLines, ExternalPO,
#         FulfillmentMethod, IsDropShip, Password, PaymentMethod, PurchaseOrderNumber, ShipToAddress1, ShipToCity,
#         ShipToCountryCode, ShipToName, ShipToPostalCode, ShipToStateProvince, ShipVia, UserId, SignatureRequired,
#         BillingCardAddress1, BillingCardCity, BillingCardCountryCode, BillingCardPostalCode, BillingCardStateProvince,
#         CreditCardNumber, ExpirationMonth, ExpirationYear, SaveForFutureUse
#     ]

#     if all(item != "" for item in compulsoryFieldsList):
#         print("Empty string test Test Passed")
#     else:
#         return "Empty string detected, Provide all values for Compulsory fields"

#     if all(item is not None for item in compulsoryFieldsList):
#         print("Not None Test Passed")
#     else:
#         return "None/Null value detected, Provide all values for Compulsory fields"


#     client = Client(wsdl="https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl")
#     CreditCardPurchaseOrderRequestType = client.get_type("ns2:CreditCardPurchaseOrderRequest")

#     CreditCardPurchaseOrderRequestElement = CreditCardPurchaseOrderRequestType(
#         BypassAddressValidation,
#         ConfirmToEmailAddress,
#         ConfirmToName,
#         CreditCardCV2,
#         DealerAccountNumber,
#         DetailLines,
#         ExternalPO,
#         FulfillmentMethod,
#         IsDropShip,
#         KrollVaultCreditCardDescription,
#         Password,
#         PaymentMethod,
#         PurchaseOrderNumber,
#         ShipToAddress1,
#         ShipToAddress2,
#         ShipToAddress3,
#         ShipToCity,
#         ShipToCountryCode,
#         ShipToName,
#         ShipToPostalCode,
#         ShipToStateProvince,
#         ShipToTelephoneNumber,
#         ShipVia,
#         SignatureRequired,
#         UserId,
#         BillingCardAddress1,
#         BillingCardCity,
#         BillingCardCountryCode,
#         BillingCardPostalCode,
#         BillingCardStateProvince,
#         CreditCardNumber,
#         ExpirationMonth,
#         ExpirationYear,
#         SaveForFutureUse
#     )

#     return client.service.SubmitCreditCardPurchaseOrder(CreditCardPurchaseOrderRequestElement)


# def AddressToValidate(
#     Address1: str,
#     Address2: str,
#     City: str,
#     Country: str,
#     PostalCode: str,
#     State: str
# ) -> dict:
#     client = Client(wsdl="https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl")
#     AddressToValidateType = client.get_type("ns2:AddressToValidate")


# def CheckProductAvailability( DealerAccountNumber: str | None  = None, Password: str | None  = None, SkuList :list[str] | None = None,  UserId: str | None = None ) -> dict:

#     if SkuList == None:
#         return "SkuList Must be Provided !!!"

#     if DealerAccountNumber == None:
#         DealerAccountNumber = "18882"
#     if Password == None:
#         Password = "48e000f8bf98457caa78bfcc0b14d3e8"
#     if UserId == None:
#         UserId = "purchasing@ecoppolicesupply.com"

#     client = Client(wsdl="https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl")
#     CheckProductAvailabilityRequestType = client.get_type("ns2:CheckProductAvailabilityRequest")

#     CheckProductAvailabilityRequestElement = CheckProductAvailabilityRequestType( DealerAccountNumber, Password, SkuList, UserId )

#     return client.service.CheckProductAvailability(CheckProductAvailabilityRequestElement)
