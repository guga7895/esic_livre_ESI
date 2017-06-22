# URL para a base de dados
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{senha}@localhost/{base}'

# Credenciais usadas para interagir com o eSIC do municipio de São Paulo
ESIC_EMAIL = "{email}"
ESIC_PASSWORD = "{senha}"

# Caminho para o executavel do firefox usaod pelo selenium
# MUITO IMPORTANTE NOTAR QUE O CAMINHO DEVE APONTAR DIRETAMENTE PARA
# O EXECUTAVEL DO PROGRAMA
FIREFOX_PATH = "/path/to/firefox/executable"

# Caminho para uma pasta onde serão guardados temporariamente os arquivos .wav
# baixados para quebrar o catcha do eSIC
DOWNLOADS_PATH = "/path/to/downloads"

# Prefixo de onde serão guardados os arquivos em anexo mandados do eSIC do
# municipio de Sao Paulo como resposta de volta para o esiclivre
ATTACHMENT_URL_PREFIX = '{prefix}'

# Pasta para armazenar os logs do sistema
LOG_FOLDER = '/path/to/LOG_FOLDER'
