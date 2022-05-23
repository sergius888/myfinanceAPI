# step1: read the file or database
print("STEP1: Reading the file ...")
file = open(
    "../my_finance/database/database.txt"
)  # in path, a single dot . -> current directory, .. -> parent directory
contents = file.read()
file.close()
import json

stocks = json.loads(contents)

print("STEP2: Adding longSummary & exchange info to current data ...")
import yfinance

for s in stocks:  # stocks is a list of dicts
    print("Adding new data for this stockk info ... ", s)
    yf_ticker = yfinance.Ticker(s["ticker"])
    long_summary = yf_ticker.info["longBusinessSummary"]
    exchange = yf_ticker.info["exchange"]
    s["longSummary"] = long_summary
    s["exchange"] = exchange
    print("Added new data, new stockk info: ", s)

print("STEP3: Save to file (or database)")
new_content = json.dumps(stocks, indent=2)
file = open("../my_finance/database/database.txt", "w")
file.write(new_content)
file.close()
