# psexec -u svc-certreq-prd@fpprod.corp -p sG8Yms%#Qh certreq -submit -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll"
# psexec -u svc-certreq-prd@fpprod.corp -p sG8Yms%#Qh cmd
# runas /noprofile /user:svc-certreq-prd@fpprod.corp cmd
# sG8Yms%#Qh
# certreq -submit -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll\nsan:dns=altname1&dns=altname2&dns=altname3" mycertreq.csr
# certreq -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll"
# certreq -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll" pki_test.csr
# certreq -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll" pki_test.csr certificate.csr
# certreq -submit -f -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll" -config "CHVIRPKIPRD103.fpprod.corp\Leonteq Class 3 Issuing CA" pki_test.csr certificate.csr
# certreq -submit -f -attrib "CertificateTemplate:LeonteqWebSrvManualEnroll" -config "CHVIRPKIPRD103.fpprod.corp\Leonteq Class 3 Issuing CA" C:\\Users\Public\pki_test.csr C:\\Users\Public\certificate.csr
import tempfile
import os

CSR_STORE_DIR = tempfile.gettempdir()
CERT_STORE_DIR = tempfile.gettempdir()

template = r'"CertificateTemplate:LeonteqWebSrvManualEnroll"'
domain = r'"CHVIRPKIPRD103.fpprod.corp\Leonteq Class 3 Issuing CA"'
csr_path = r'C:\\projects\pki_bridge_main_service\src\test_data\pki_test.csr'
cert_path = r'C:\\Users\Public\certificate.csr'

commands = [
    'certreq',
    '-submit',
    '-f',
    '-attrib',
    template,
    '-config',
    domain,
    csr_path,
    cert_path,
]
command = ' '.join(commands)
os.system(command)
