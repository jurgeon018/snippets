
import subprocess



def run(args):
    p = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    result = p.communicate()
    if not p.returncode == 0:
        raise Exception(f'returncode is 0. args: {args}')
    result = result[0]
    return result



command = r'certutil -config "CHVIRPKIPRD103.fpprod.corp\Leonteq Class 3 Issuing CA" -CATemplates'
results = run(command)

print(type(results))
# results = str(results)
print()
print(results.split('\r\n'))
print()


