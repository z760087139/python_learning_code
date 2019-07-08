import ldap, json

def ldap_login(ldap_path, user, domain, passwd):
    try:
        c = ldap.initialize(ldap_path)
        c.protocol_version = ldap.VERSION3
        d = c.simple_bind("%s@%s"%(user, domain), passwd)
    except ldap.INVALID_CREDENTIALS as e:
        c.unbind()
        c = d = None
    finally:
        return c, d

def user_info(c, user, base):
    try:
        scope  = ldap.SCOPE_SUBTREE
        filterstr = "(sAMAccountName=%s)"%user

        id = c.search(base, scope, filterstr, None)

        result_type, result_data = c.result(id, 1)
        return result_data
    except ldap.LDAPError as e:
        return None
    finally:
        pass

####

ldap_path = "ldap://192.168.22.129:389"
base = "DC=dev,DC=com"
user = "test"
domain = "dev.com";
passwd = "1qaz@WSX";

c, d = ldap_login(ldap_path, user, domain, passwd)

if c == None:
    print "login error!"
    exit(1)

print "user: %s login ok!"%user
info = user_info(c, user, base)
print json.dumps(info, ensure_ascii=False, indent=4)

c.unbind()



