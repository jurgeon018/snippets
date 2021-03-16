
import ldap
ad = ldap.initialize("ldap://fpprod.corp")
x = ad.simple_bind_s("FpprodLdap", "P455word")
print(x)