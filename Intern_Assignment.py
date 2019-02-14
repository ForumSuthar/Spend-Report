# -*- coding: utf-8 -*-

#!/usr/bin/env python

"""Generating Spend Report
Function name: spend_reporter.
This function is used to calculate total amount spend by each vendor on different products and generate a report.
"""        

def spend_reporter():
    try:
        sorted_data = csv_read()
        spend_reporter_dict = computing_spend(sorted_data)
        display_data(spend_reporter_dict)
    except Exception as e:
        print(e)
                 

"""Reading Input CSV
Function name: csv_read.
This function is used to read csv input from command line and 
returns a  dictionary sorted alphabetically based on first Product names and then Vendor names.
"""
def csv_read():
    try:
        import csv
        import sys
        filename = sys.argv[1]
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)    
            sorted_data = sorted(csv_reader, key=lambda row: row["Product"], reverse=False)
            sorted_data = sorted(sorted_data, key=lambda row: row["Vendor"], reverse=False)
        return sorted_data
    except Exception as e:
        print(e)

"""Calculating Total Spend
Function name: computing_spend.
This function is used to calculate the total spend by vendors on each product and  
returns a  dictionary with the following values:
Vendor:
    Product: total spend on this product
    Total: total spend overall by this vendor

"""
def computing_spend(sorted_data):
    try:
        spend_reporter_dict = {}
        #appending the values in a new dictionary
        #spend_reporter_dict = {Vendor:{Product1:total spend,Product2:total spend,---,Total:total spend overall}}.
        for row in sorted_data:
            vendor = row["Vendor"]
            product = row["Product"]
            amount = row["Amount"]
            amount = int(amount)
            if vendor not in spend_reporter_dict:
                #if vendor is not present in dictionary then add
                spend_reporter_dict[vendor] = {}
                spend_reporter_dict[vendor][product]=amount
                spend_reporter_dict[vendor]["Total"] = amount
            else:
                #if product not present in dictionary then add
                if product not in spend_reporter_dict[vendor]:              
                    spend_reporter_dict[vendor][product]=amount
                else:
                    #if product repeated, update the value with sum of the amount spend on that product
                    sum = spend_reporter_dict[vendor].get(product)
                    sum+=amount
                    spend_reporter_dict[vendor].update({product:sum})
                #update the value with sum of the amount spend overall by the vendor
                total = spend_reporter_dict[vendor].get("Total")
                total+=amount
                spend_reporter_dict[vendor].update({"Total":total})
        return spend_reporter_dict
    except Exception as e:
        print(e)
 
"""Printing Total Spend
Function name: display_data.
This function is used to print all the computed values in an Easy-to-read format

"""           
def display_data(spend_reporter_dict):
    #For printing the values
    try:
        for vendor,data in spend_reporter_dict.items():
            total = "$"+"{:,}".format(data["Total"]) #converting int into price format
            print(vendor,total)
            for product,amount in data.items():
                if(product == "Total"):
                    continue
                else:
                    sum = "$"+"{:,}".format(amount)
                    print("  ",product,sum)
    except Exception as e:
        print(e)

     
spend_reporter()              
        

