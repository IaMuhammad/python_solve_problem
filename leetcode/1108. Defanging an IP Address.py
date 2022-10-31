def ipAdress(address):
        i = 0
        address1 = ''
        while i < len(address):
                if address[i] == '.':
                        address1 += '[.]'
                else:
                        address1 += address[i]
                i += 1
        return address1

a = str(input())
print(ipAdress(a))