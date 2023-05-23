from pydantic import BaseModel


class CheckOrderStatusRequestBody(BaseModel):
    DealerAccountNumber: str | None = None
    OrderConfirmationNumber: str | None = None
    Password: str | None = None
    UserId: str | None = None


class SubmitPurchaseOrderRequestBody(BaseModel):
    BypassAddressValidation: bool = True
    ConfirmToEmailAddress: str = ""
    ConfirmToName: str = ""
    CreditCardCV2: str = ""
    DealerAccountNumber: str = ""
    DetailLines: list[dict] 
    ExternalPO: str = ""
    FulfillmentMethod: str
    IsDropShip: bool
    KrollVaultCreditCardDescription: str = ""
    Password: str = ""
    PaymentMethod: str
    PurchaseOrderNumber: str = ""
    ShipToAddress1: str = ""
    ShipToAddress2: str = ""
    ShipToAddress3: str = ""
    ShipToCity: str = ""
    ShipToCountryCode: str = ""
    ShipToName: str = ""
    ShipToPostalCode: str = ""
    ShipToStateProvince: str = ""
    ShipToTelephoneNumber: str = ""
    ShipVia: str
    SignatureRequired: bool = False
    UserId: str = ""
