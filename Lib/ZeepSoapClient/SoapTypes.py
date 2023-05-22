from zeep import Client
from typing import Optional

wsdl = "https://apiv2.krollcorp.com/EBusinessTest/Kroll.Dealer.EBusiness.svc/Docs?singleWsdl"


def PurchaseOrderDetailLineType(
    LineNumber: Optional[int] = None,
    QuantityOrdered: Optional[int] = None,
    Sku: Optional[str] = None,
):
    if all(field != "" for field in [LineNumber, QuantityOrdered, Sku]):
        # print("Empty String Test Passed\n")
        pass
    else:
        return "Purchase Order Detail Line Fields are compulsory"

    if all(field is not None for field in [LineNumber, QuantityOrdered, Sku]):
        # print("Not None Test Passed\n")
        pass
    else:
        return "Purchase Order Detail Line Fields are compulsory"

    client = Client(wsdl=wsdl)
    PurchaseOrderDetailLineType = client.get_type("ns2:PurchaseOrderDetailLine")

    return PurchaseOrderDetailLineType(LineNumber, QuantityOrdered, Sku)


def ArrayOfPurchaseOrderDetailLineType(
    PurchaseOrderDetailLineArray: Optional[list[dict]],
):
    # passed to DetailLine Parameter

    client = Client(wsdl=wsdl)

    if isinstance(PurchaseOrderDetailLineArray, list) and all(
        isinstance(item, dict) for item in PurchaseOrderDetailLineArray
    ):
        ArrayOfPurchaseOrderDetailLineType = client.get_type(
            "ns2:ArrayOfPurchaseOrderDetailLine"
        )
        NewPurchaseOrderDetailLineArray = [
            PurchaseOrderDetailLineType(
                record["LineNumber"], record["QuantityOrdered"], record["Sku"]
            )
            for record in PurchaseOrderDetailLineArray
        ]
        return ArrayOfPurchaseOrderDetailLineType(NewPurchaseOrderDetailLineArray)

    else:
        return "Array/List Supplied Must be of type list[dict] example \n\t '[{ 'LineNumber': type(int), 'QuantityOrdered': type(int), 'Sku': type(str)}]'"


def FulfillmentMethodType(value: Optional[str] = None):
    client = Client(wsdl=wsdl)
    FulfillmentMethodType = client.get_type("ns2:FulFillmentMethod")
    option_1 = "ShipProductThatIsAvailableNowAndOtherProductWhenAvailable"
    option_2 = "RejectOrderIfAllProductsAreNotAvailable"
    errorMessage = (
        f"Fullfillment Method requires either:\n\tvalue ({option_1}, {option_2})"
    )

    if value is None:
        return errorMessage

    if value == option_1:
        return FulfillmentMethodType(option_1)
    elif value == option_2:
        return FulfillmentMethodType(option_2)
    else:
        return errorMessage


def PaymentMethodType(value: Optional[str] = None):
    client = Client(wsdl=wsdl)
    PaymentMethodType = client.get_type("ns2:PaymentMethod")

    option_1 = "AccountTerms"
    option_2 = "CreditCard"
    errorMessage = (
        f"Accecpted Payment Method are Either:\n\tvalue ({option_1}, {option_2})"
    )

    if value == None:
        return errorMessage

    if value == option_1:
        return PaymentMethodType(option_1)
    elif value == option_2:
        return PaymentMethodType(option_2)
    else:
        return errorMessage


def ShipViaType(method: Optional[str] = None):
    client = Client(wsdl=wsdl)
    ShipViaType = client.get_type("ns2:ShipVia")

    option_1 = "FlatRate"
    option_2 = "Ground"
    option_3 = "SecondDayAir"
    option_4 = "NextDayAir"
    errorMessage = f"Accepted ShipVia Methods :\n\t({option_1}, {option_2}, {option_3}, {option_4})"

    if method == None:
        return errorMessage

    if method == option_1:
        return ShipViaType(option_1)
    elif method == option_2:
        return ShipViaType(option_2)
    elif method == option_3:
        return ShipViaType(option_3)
    elif method == option_4:
        return ShipViaType(option_4)
    else:
        return errorMessage


# client = Client(wsdl=wsdl)
# ArrayOfPurchaseOrderDetailLineType = client.get_type("ns2:ArrayOfPurchaseOrderDetailLine")
# print(ArrayOfPurchaseOrderDetailLineType)
# Tests for types

# detailline = PurchaseOrderDetailLineType(LineNumber=1,QuantityOrdered=1 ,Sku="TSP-5554219006")
# print(str(type(detailline)))

# DetailLineDictionaryArray =[
#     { 'LineNumber': 1, 'QuantityOrdered': 1, 'Sku': 'TSP-5554219006'},
#     { 'LineNumber': 2, 'QuantityOrdered': 1, 'Sku': 'STRE-69280'},
#     { 'LineNumber': 3, 'QuantityOrdered': 1, 'Sku': 'A56001'},
#     { 'LineNumber': 4, 'QuantityOrdered': 1, 'Sku': 'STRE-69282'}
# ]
# testList = ["Hello", "there"]
# testList2 = [ 1,2,3]

# print(ArrayOfPurchaseOrderDetailLineType(DetailLineDictionaryArray))
# print(ArrayOfPurchaseOrderDetailLineType(testList))
# print(ArrayOfPurchaseOrderDetailLineType(testList2))

# print(FulfillmentMethodType())
