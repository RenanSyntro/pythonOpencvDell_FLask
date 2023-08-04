# Caminho para o ambiente virtual (altere para o caminho correto)
$envPath = "caminho\para\seu\env\Scripts\activate"

# Caminho para o arquivo Python da aplicação (altere para o caminho correto)
$pythonAppPath = "caminho\para\pasta\do\seu\projeto\nome_do_arquivo_da_sua_aplicacao.py"

# Ativar o ambiente virtual e iniciar a aplicação Python
& $envPath
python $pythonAppPath