# -*- coding: utf-8 -*-

import csv
import sys
filename = sys.argv[1]
with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    sortedlist = sorted(csv_reader, key=lambda row: row["Product"], reverse=False)
    sortedlist = sorted(sortedlist, key=lambda row: row["Vendor"], reverse=False)
    spend_reporter_dict = {}
    #appending the values in a dictionary
    for row in sortedlist:
        vendor = row["Vendor"]
        product = row["Product"]
        amount = row["Amount"]
        amount = int(amount)
        if vendor not in spend_reporter_dict:
            spend_reporter_dict[vendor] = {}
            spend_reporter_dict[vendor][product]=amount
            spend_reporter_dict[vendor]["Total"] = amount
        else:
            if product not in spend_reporter_dict[vendor]:              
                spend_reporter_dict[vendor][product]=amount
            else:
                sum = spend_reporter_dict[vendor].get(product)
                sum+=amount
                spend_reporter_dict[vendor].update({product:sum})
            total = spend_reporter_dict[vendor].get("Total")
            total+=amount
            spend_reporter_dict[vendor].update({"Total":total})
            
    #For printing the values
    for vendor,data in spend_reporter_dict.items():
        total = "$"+"{:,}".format(data["Total"])
        print(vendor,total)
        for product,amount in data.items():
            if(product == "Total"):
                continue
            else:
                sum = "$"+"{:,}".format(amount)
                print("  ",product,sum)
                

                
        

