cd ..
curl --location --request POST '127.0.0.1:5001/certificate' \
--header 'Content-Type: application/json' \
--data-raw '{
	"additional": {"Subject": "CN=W2K8-B0-DC.contoso2.com"}
}'

