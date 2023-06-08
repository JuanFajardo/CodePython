
users = ['1111', '666666', '888888', 'Admin', 'Administrator', 'Dinion', 'Root', 'admin', 'admin1', 'guest', 'netadmin', 'root', 'service', 'supervisor', 'sysadmin', 'test', 'ubnt', 'user', 'web', 'webadmin']

passs= ['', ' ', '00000000', '1111', '1111111', '123123', '1234', '12345', '123456', '123asdfg', '4321', '666666', '888888', '9999', 'Admin', 'Pass', 'admin', 'admin123', 'asdfg123', 'fliradmin', 'fliradmin', 'ikwb', 'jvc', 'meinsm', 'pass', 'password', 'qwerty', 'root', 'service', 'supervisor', 'system', 'system', 'ubnt', 'user', 'wbox', 'wbox123', '123abc', 'abc123']

for u in users:
    for p in passs:
        print(f'{u}:{p}')
