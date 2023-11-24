#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - ротируемый прокси
proxy_login = 'gmail_com-country-be'
proxy_password = 'xxxxxxx'
proxy_address = 'some.address.com'
proxy_port = '8080'

amount_wallets_in_batch = 1

#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 1200}
else:
    request_kwargs = {"timeout": 120}

