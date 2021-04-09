import os
import subprocess
import tempfile
import logging as log

from flask import Flask, request, jsonify

import configparser


app = Flask(__name__)
CSR_STORE_DIR = tempfile.gettempdir()
CERT_STORE_DIR = tempfile.gettempdir()
CERTREQ_PATH = "certreq"




def submit(template_name, domain, request):
    csr_filepath = os.path.join(CSR_STORE_DIR, "csr.req")
    with open(csr_filepath, 'w') as csr_file:
        csr_file.write(str(request))
        csr_file.close()
    cert_filepath = os.path.join(CERT_STORE_DIR, "csr.cer")
    if template_name == 'WebServerAndClientAuth':
        template = "-attrib CertificateTemplate:WebServerAndClientAuth"
    elif template_name == 'WebServer':
        template = "-attrib CertificateTemplate:WebServer",
    run_args = [
        CERTREQ_PATH,
        template,
        '-submit',
        '-f',
        '-q',
        '-config',
        domain,
        csr_filepath,
        cert_filepath,
    ]
    subprocess.run(run_args)
    result_cert = None
    with open(cert_filepath, 'r', encoding='utf-8') as cert_file:
        result_cert = cert_file.readlines()
        cert_file.close()
    return result_cert


@app.route('/certificate', methods=['POST'])
def certificate():
    content = request.json
    domain = content['domain']
    csr = content['request']
    template = content['template']
    try:
        result_cert = submit(template, domain, csr)
    except Exception:
        err_msg = "cannot start certreq to submit CSR"
        log.exception(err_msg)
        return jsonify({'error': err_msg}), 500
    return jsonify({'result': result_cert})
