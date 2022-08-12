#!/usr/bin/python3
# Modem Claro Kaon CG3000

import requests


MD5_USUARIO = "00000000000000000000000000000000"
MD5_SENHA = "00000000000000000000000000000000"

DADOS = {
    'login_id': MD5_USUARIO,
    'login_pw': MD5_SENHA
}

URL_LOGIN = "http://192.168.0.1/logincheck.cmd"

sessao = requests.Session()

try:
    resposta_login = sessao.post(URL_LOGIN, data=DADOS, timeout=3)
    resposta_login.raise_for_status()
except Exception as e:
    print("Erro:", e)
    exit()

URL_REBOOT = "http://192.168.0.1/rebootinfo.cgi?path_name=resetrouter.html"

try:
    resposta_reboot = sessao.get(URL_REBOOT, timeout=3)
    resposta_reboot.raise_for_status()
except Exception as e:
    print("Erro:", e)
    exit()
