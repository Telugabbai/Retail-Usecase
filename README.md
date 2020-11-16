# Retail-Usecase

ABC stores is a chian of retail stores, serving the customers world-wide,with a wide range of products 
like groceries,home decor,furniture.electronics etc.,

ABC stores has 400+ retail stores,selling world-wide and generating the sales data at their POS(Point Of Sales)Systems

The daily data from the POS systems world-wide,gets pushed into the Big-data pipelines for cleaning,processing and Bussiness analysis.

ABC has huge no.of stores they will be pushing the daily sales data from their online server to our big data pipelines

Along with that, we have to consider some bussiness data dirtectly from ABC- Stores headquaters.


Bussiness Requirements:

coliumns in daily sales data:

Sale_ID,Prodct_ID,Quantity_Sold,Vendor_ID,Sale_Date,Sale_Amount,Sale_Currency.

Conditons:

-> Due to network failure columns might be missing
  . If missing
     . Quantity_Sold --- Hold the data till updates received
	 . Vendor_ID ---- Hold the data till updates received

-> Release the hold records in case the updates of the missing value is received in consecutive day's data	
   (Starts the processing)

-> If sale_amount not received 
  . Derive from the product price,provided by the headquaters, considering the sale_currency's exchange rate in USD.


->Get the vendor details from the bussiness data and bind with the final extract, for repoting and analysis.

-> Get the complete sales data, per sale_ID, to be fetched into the reports.

