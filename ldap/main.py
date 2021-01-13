import ldap 

# ad = ldap.initialize("ldap://192.168.0.16")
ad = ldap.initialize("ldap://ldap.forumsys.com")
print(ad)
x = ad.simple_bind_s("tesla", "password")
print(x)
# (97, [], 1, [])