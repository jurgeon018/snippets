# https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/
# https://knowledge.digicert.com/solution/SO26449.html
# https://www.sslshopper.com/article-most-common-openssl-commands.html

# PEM, Base64 ASCII(.crt, .pem, .cer, .key, .ca-bundle, .....)
# DER, binary(.der, .cer)

# PEM containers:
# PKCS #12 , (.p12, .pfx)
# PKCS #7 (.p7b)

###########

# x509 -> PEM
# openssl x509 -in src/dev/www.ssl.com.x509 -outform PEM -out src/dev/www.ssl.com3.pem

# View pem
# openssl x509 -in src/dev/www.ssl.com.pem -text -noout 

# pem -> der
# openssl x509 -outform der -in src/dev/www.ssl.com.pem -out src/dev/www.ssl.com.der

# View der
# openssl x509 -inform der -in src/dev/www.ssl.com.der -text -noout

# der -> pem
# openssl x509 -inform der -in src/dev/www.ssl.com.der -out src/dev/www.ssl.com.pem
# openssl x509 -inform der -in src/dev/www.ssl.com.der -outform pem -out src/dev/www.ssl.com.pem


# PEM -> PKCS7(P7B)
# openssl crl2pkcs7 -nocrl -certfile certificatename.pem -out certificatename.p7b -certfile CACert.cer

# PKCS7(P7B) -> PEM
# openssl pkcs7 -print_certs -in certificatename.p7b -out certificatename.pem

# pfx -> PEM
# openssl pkcs12 -in certificatename.pfx -out certificatename.pem

# PFX -> PKCS#8
# STEP 1: PFX -> PEM
# openssl pkcs12 -in certificatename.pfx -nocerts -nodes -out certificatename.pem
# STEP 2: PEM -> PKCS8
# openSSL pkcs8 -in certificatename.pem -topk8 -nocrypt -out certificatename.pk8

# P7B -> PFX
# STEP 1: P7B -> CER
# openssl pkcs7 -print_certs -in certificatename.p7b -out certificatename.cer
# STEP 2: CER -> Private Key to PFX
# openssl pkcs12 -export -in certificatename.cer -inkey privateKey.key -out certificatename.pfx -certfile  cacert.cer


# Convert PEM certificate with chain of trust to PKCS#7
# openssl crl2pkcs7 -nocrl -certfile CERTIFICATE.pem -certfile MORE.pem -out CERTIFICATE.p7b

# Convert PEM certificate with chain of trust and private key to PKCS#12
# openssl pkcs12 -export -out CERTIFICATE.pfx -inkey PRIVATEKEY.key -in CERTIFICATE.crt -certfile MORE.crt

# Convert a PEM certificate file and a private key to PKCS#12 (.pfx .p12)
# openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt

# Convert a PKCS#12 file (.pfx .p12) containing a private key and certificates to PEM
# openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes
