import csv
from datetime import datetime   
import pytz

# Get trades
trades={}
local = pytz.timezone('America/Puerto_Rico')

with open('./input.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    o= []
    o.append("ActivityType")
    o.append("DateTime")
    o.append("TransDateTime")
    o.append("Symbol")
    o.append("OrderActionSource")
    o.append("InternalOrderID")
    o.append("ServiceOrderID")
    o.append("OrderType")
    o.append("Quantity")
    o.append("BuySell")
    o.append("Price")
    o.append("Price2")
    o.append("OrderStatus")
    o.append("FillPrice")
    o.append("FilledQuantity")
    o.append("TradeAccount")
    o.append("OpenClose")
    o.append("ParentInternalOrderID")
    o.append("PositionQuantity")
    o.append("FillExecutionServiceID")
    o.append("HighDuringPosition")
    o.append("LowDuringPosition")
    o.append("Note")
    o.append("AccountBalance")
    o.append("ExchangeOrderID")
    o.append("ClientOrderID")
    o.append("TimeInForce")
    o.append("Username")
    o_str = '\t'. join(o)
    print(o_str)
    
    for row in reader:
        # print(row[0])
        # print(row[11])
        if row[11].strip()=="Filled" :
            output = []

            # ActivityType
            output.append("Orders")

            # DateTime
            naive = datetime.strptime(row[9].strip(), "%m/%d/%Y %H:%M:%S")
            local_dt = local.localize(naive, is_dst=None)
            utc_dt = local_dt.astimezone(pytz.utc)

            output.append(utc_dt.strftime("%Y-%m-%d %H:%M:%S"))

            # TransDateTime
            output.append(utc_dt.strftime("%Y-%m-%d %H:%M:%S"))

            # Symbol
            output.append("@ES#")

            # OrderActionSource
            output.append(row[6].strip())

            # InternalOrderID
            output.append("")

            # ServiceOrderID
            output.append("")

            # OrderType
            output.append("Limit")

            # Quantity
            output.append(row[8].strip())

            # BuySell
            output.append(row[3].strip())

            # Price
            output.append(row[27].strip())

            # Price2
            output.append("")

            # OrderStatus
            output.append("Filled")

            # FillPrice
            output.append(row[27].strip())

            # FilledQuantity
            output.append(row[8].strip())

            # TradeAccount
            output.append("tradovate")

            # OpenClose
            output.append("Close")

            # ParentInternalOrderID
            output.append("")

            # PositionQuantity
            output.append("")
            
            # FillExecutionServiceID
            output.append(row[0].strip())

            # HighDuringPosition
            output.append("")

            # LowDuringPosition
            output.append("")

            # Note
            output.append("")

            # AccountBalance
            output.append("0")

            # ExchangeOrderID
            output.append("")

            # ClientOrderID
            output.append("")

            # TimeInForce
            output.append("Day")

            # Username
            output.append("")

            output_str = '\t'. join(output)
            print(output_str)
