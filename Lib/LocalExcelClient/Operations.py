import polars as pl
import os
pl.Config.set_tbl_cols(5).set_tbl_rows(5).set_fmt_str_lengths(12)

def getAllRecords() -> pl.DataFrame:
    
    root_dir = os.getcwd()
    excel_file = root_dir + "/Lib/LocalExcelClient/Data/K052121-01.xlsx"
    all_records = pl.read_excel(excel_file).fill_null("")
       
    return all_records


def getCustomerData() -> list[dict]:
    all_records = getAllRecords()
    columns = all_records.columns

    columns = all_records.columns
    customerData = (
        all_records.filter(
            ((pl.col(columns[0]).is_not_null()) & (pl.col(columns[0]) != ""))
        )
        .select(columns[0:11])
        .to_dicts()
    )

    return customerData


def getPurchaseOrderNumber() -> dict:
    customerData = getCustomerData()
    columns = list(customerData[0].keys())

    return {
        "PurchaseOrderNumber": customerData[0][columns[0]],
        "Shipping": customerData[0][columns[9]],
    }


def getCustomerNameContact() -> dict:
    customerData = getCustomerData()
    columns = list(customerData[0].keys())

    return {
        "FirstName": customerData[0][columns[1]],
        "LastName": customerData[0][columns[2]],
        "CompanyName": customerData[0][columns[3]],
        "PhoneNumber": customerData[0][columns[10]],
    }


def getCustomerAdresses() -> dict:
    customerData = getCustomerData()
    columns = list(customerData[0].keys())

    return {
        "address1": customerData[0][columns[4]],
        "address2": customerData[0][columns[5]],
        "city": customerData[0][columns[6]],
        "state": customerData[0][columns[7]],
        "zipcode": customerData[0][columns[8]],
    }


def getSkuList() -> list[str]:
    all_records = getAllRecords()
    columns = all_records.columns[12]

    return all_records.select(columns).to_dict(as_series=False)[columns]


def getDetailLineArray() -> list[dict]:
    all_records = getAllRecords()
    columns = all_records.columns[12:14]
    all_records = all_records.rename({columns[0]: "Sku", columns[1]: "QuantityOrdered"})

    updateColumns = ["QuantityOrdered", "Sku"]
    detailList = all_records.select(updateColumns).to_dicts()
    for index in range(0, len(detailList)):
        detailList[index]["LineNumber"] = index + 1

    return detailList
