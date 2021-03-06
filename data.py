def get_logindata(user, pswd, mode=True):
    if mode:
        data = {
            'username': '{}'.format(user),
            'password': '{}'.format(pswd)
        }
        return data
    else:
        data = {
            "username": "{}".format(user),
            "password": "{}".format(pswd),
            'execution': '228c85c3-5f9f-4a81-b78c-2ea36bcfcde9_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuS1NTOGZObVFKUG96YkVzZ1NVdDd4dys5Um1QR0tub3k1YUNscFhSWVJ5Y1hMUjJ3VUN4TmpFMHd2SEkwTWNYTmlVaXNlTVZwcDZlZldOUFV5K2tuWkk1UlRDZEJVR3orY2VqeHJwOU5jZHNFKzZ0cG83d2M2NTdPZE13bVFuUTBPK0JITDcvdGMvbjhyWVFMdktEdDAyckVaTlNmZjJzdlc5d0J6TlIxemMwV2dieU9rVTVqaXZUVWI1TTJDMHdEeFQ3Y3grMGg0OGpUNDkyOG9wVGdMc1BDR3hvdE1MQ2I4ZHhFbTR3N1hzUElPMC9xSGJMbWxvWUhyM3VmcThRQkh3OVJvaEVjRmlBQTdEQXJma0hBditaZjNjWWVSeFFzMmIzUmhKTDVlYWRQeTdUeTNXOEJVeVY5SFJvUzI0ZUxhVWg4ZGlrVmdEeWNoVTF1WGV2QjZiZ0YwcHg2VlpFNnNXTzV1Q1Y4aG5DS3RKWVFqN1pNZ1ZhTGVMcGdtYWFPOTZNOVZrcmdyMmJkOFNDSzB2c09oenMrVVI2ZXZBUTZoTXNudG9mR3VHQk5uSmxTdXNZd2M4VnBCUnBkT2d5bWJIcitxMHdQMno0VnVvdnBPVHgwVkg3TkYxamwwWGhtNG11b3RFaUFKd2pMMUFXUVpjaDZVWnhCdG1BWHZCMUV2WFJMVmxZYUxRT0FIK3lhSnZYRE93VGpQTTZ1K3kybUNTbkswbC8vWEl5VWhxUVFISTRjcS9hUHpUbkkrZmVORVM2TmEvZ0cvQ0tPejQ4bEpoUHZ2OVRyYzNqV2lKb1I2Mmo3ek9USHEwc3c0cyt2MDRPcHZrakpGZStNRUNMdG9ZejJZbXNHMTNkci9lMDl3bHNkWEN3TkVhT3JNTDR2MkRSMGd3Znh1aU12NEo1cjYrRHpZYjQzZHQ3VUZjdFgxNnl2dW9MaVhFbkFLTFFSdjkvc1JBTGpINWx0UmJwdE01bWRWUjJTS3NMZTRQSEtySE1Xd2F5djZPdEpvOUI1bjRtajQ1N21sNy9XLzY1dWpOQTF5bkVTRWl0Rk15Mm53dWFjdkhickZjSnRtVnBHNy9RN1RTSVc1Z1M2K2xTcldxVGszMUFPanZvMzN5NmlkbUx3WTI0SHk1dkZiTkJRMjBlUFRHdkM5Zk9YczBsNjd2dFRsZUI3Y3o0d0hGV1c5cEFER3dnZU90cGRlWmdmU3NJZXkwUUNpZXFKUE5ERFVrS2V3Y2kvYTlZM1lPMzhvdkVPYTlDYWhteUxtcXRyb1MrdTRkTUJGYklwd3FKUUZKa1BYYnNINFo4NHFQNzhzTnZENCtyUWZYUm43WlE0VWoyLzZDR1FJN05sQ00wb2c0dUIycmp1NjV4S3VBd3FwRS9temkwYzFSandPdGZsK1JzWTlwV1hsTHNhYldvMEl0Y09OVVZCbnJGeDU5RjBMdDFVQ0FjaG5SQTBmMlVwVGVmZFZnODJveGdQRUNHdjk1NXc2S1crNGxLNmdTcjB3TFg5b3NoakwwWjJPbkIrVUF3ZWJzYkFFTkhYeENBRGUrbFUvM1pKcG1qWitoZ0Q5RGhzMUlDSTFmaWJEVHlnbGJ1Q1NnRVFvVjZSNmNreDBKWE1QL3VOZFBwOWVYWFpEa2gzeFJtZ3Y3YjhwTFJzejNlaUhXRittQnRaei9kb0JGLzZ5ekJveTFPNGQ4UTFjTVJpL2ZoV3QrQjNpcmpkanRaTkNuYmFEbHZtb2IzWVVUWVBwQTdCRFlJRzF5b1IvWU5TcWFhVlBBdVhZVUk1NEdYeW8yYlQ0b2xPTHJrK2tKYWZGNXZTOGNBN1l1VWpGR3c4Rjd6OFlOZ2pmYzBBa3BTN1dwWlVSS3kwUVRndWYvUmFqZzBNaGNnWlM2SWtGYVhOeWRTdHlXUkVMNkdPMi9IbTdLNkdIVyt3TmpjYkpXRVM5R1htNGc0Uk1GNklMdTZBZ3dZSFcvaEJNQ0dqeUNRV2h3SFhiMXhjUEIzdjlub3Joa3ljVTRRcTNhdTNLa2Q2bEVocmV3N3BmbHVDSG5lSmRtdzFLSm5sVWM2V0Q0ajJrZFVtVk9CeUQwaHUyeTByckJYclZ0OD0uUlpKaF9lc0FwVE5Oc3MtMXltb01DZ19nTHZyazFCc0d0N2h3MTdNQ2dmWi05UVNtVjBfZUt2MFA1Rm5Ub2s1SWd0QmxPRURKaDhHQUhDbE5TNE82R3c=',
            'submit': '??????',
            'type': 'username_password',
            '_eventId': 'submit'
        }
        return data
    
    
def get_postdata(data_dict):
    null = None
    true = True
    # ??????eval(dict['geo_api_info'])????????????

    data = {
        'sfzx': '{}'.format(data_dict['sfzx']),
        'tw': '{}'.format(data_dict['tw']),
        'area': '{}'.format(data_dict['area']),
        'city': '{}'.format(data_dict['city']),
        'province': '{}'.format(data_dict['province']),
        'address': '{}'.format(data_dict['address']),
        'sfcyglq': '{}'.format(data_dict['sfcyglq']),
        'sfyzz': '{}'.format(data_dict['sfyzz']),
        'qtqk': '',
        'askforleave': '{}'.format(data_dict['askforleave']),

        'geo_api_info': eval(data_dict['geo_api_info'])
    }
    # print(data)
    return data

def get_log():
    with open('Running_log', 'r') as f:
        temp = f.readlines()
        print('log is {}'.format(temp))
        return temp
