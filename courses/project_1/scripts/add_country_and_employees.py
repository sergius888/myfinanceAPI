# step1: read the file or database
print("STEP1: Reading the file ...")
file = open("../my_finance/database/database.txt")  # in path, a single dot . -> current directory, .. -> parent directory
contents = file.read()
file.close()
import json
stocks = json.loads(contents)

print("STEP2: Adding country & number of employees info to current data ...")
import yfinance
for s in stocks:  # stocks is a list of dicts
    print("Adding new data for this stock info ... ", s)
    yf_ticker = yfinance.Ticker(s["ticker"])
    s["numberOfEmployees"] = yf_ticker.info["fullTimeEmployees"]  # different line from
    s["country"] = yf_ticker.info["country"]  # different line from
    print("Added new data, new stock info: ", s)

print("STEP3: Save to file (or database)")
new_content = json.dumps(stocks, indent=2)
file = open("../my_finance/database/database.txt", "w")
file.write(new_content)
file.close()