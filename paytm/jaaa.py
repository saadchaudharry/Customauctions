# import checksum generation utility
#
# from Checksum import generate_checksum
# # initialize a dictionary
# paytmParams = dict()
#
# # put checksum parameters in Dictionary
# paytmParams["MID"] = "ZdehqP52015247605360"
# paytmParams["ORDERID"] = "YOUR_ORDER_ID_HERE"
#
# # Generate checksum by parameters we have
# # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
# checksum = generate_checksum(paytmParams, "SG4UY9spY6dyf!l6")
# print(checksum)



# import checksum generation utility
import Checksum

# # initialize JSON String
# body = "{\"mid\":\"ZdehqP52015247605360\",\"orderId\":\"pNDKGHVADGKCVDHC \"}"
#
# # Generate checksum by parameters we have in body
# # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
# checksum = Checksum.generate_checksum_by_str(body, "SG4UY9spY6dyf!l6")
# print(checksum)


paytmParams = {

	# Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"MID" : "ZdehqP52015247605360",

	# Find your WEBSITE in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"WEBSITE" : "WEBSTAGING",

	# Find your INDUSTRY_TYPE_ID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"INDUSTRY_TYPE_ID" : "Retail",

	# WEB for website and WAP for Mobile-websites or App
	"CHANNEL_ID" : "WAP",

	# Enter your unique order id
	"ORDER_ID" : "Python ",

	# unique id that belongs to your customer
	"CUST_ID" : "saad",

	# customer's mobile number
	"MOBILE_NO" : "9768890726",

	# customer's email
	"EMAIL" : "saadchaudhary646@gmail.com",

	# Amount in INR that is payble by customer
	# this should be numeric with optionally having two decimal points
	"TXN_AMOUNT" : "5000",

	# on completion of transaction, we will send you the response on this URL
	"CALLBACK_URL" : "YOUR_CALLBACK_URL",
}

# Generate checksum for parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
checksum = Checksum.generate_checksum(paytmParams, "SG4UY9spY6dyf!l6")

# for Staging
url = "https://securegw-stage.paytm.in/order/process"

# for Production
# url = "https://securegw.paytm.in/order/process"

# Prepare HTML Form and Submit to Paytm
print('<html>')
print('<head>')
print('<title>Merchant Checkout Page</title>')
print('</head>')
print('<body>')
print('<center><h1>Please do not refresh this page...</h1></center>')
print('<form method="post" action="' + url + '" name="paytm_form">')
for name, value in paytmParams.items():
	print('<input type="hidden" name="' + name + '" value="' + value + '">')
print('<input type="hidden" name="CHECKSUMHASH" value="' + checksum + '">')
print('</form>')
print('<script type="text/javascript">')
print('document.paytm_form.submit();')
print('</script>')
print('</body>')
print('</html>')