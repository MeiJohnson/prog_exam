import uuid
import random

domain = str(input('Введите домен '))
generated_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, domain)
print(generated_uuid)
