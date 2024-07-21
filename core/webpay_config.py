# core/webpay_config.py
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

# Credenciales de prueba proporcionadas por Transbank
COMMERCE_CODE = '597055555532'
API_KEY = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'

# Crear instancia de Transbank con las opciones de Webpay Plus
tx = Transaction(WebpayOptions(COMMERCE_CODE, API_KEY, IntegrationType.TEST))
