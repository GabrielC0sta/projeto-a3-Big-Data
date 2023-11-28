import pandas as pd
import mysql.connector


def convert_gasto_mensal(valor):
    try:
        print(f"Valor recebido: {valor}")
        if pd.isnull(valor):  # Verificar se o valor é nulo diretamente
            return None
        elif isinstance(valor, (int, float)):  # Se o valor já for um número, converter para o formato desejado
            if 101 <= valor <= 150:
                return 'R$101 até R$150'
            elif 301 <= valor <= 400:
                return 'R$301 até R$400'
            # Adicione mais condições para outros intervalos conforme necessário
        elif 'Acima de' in valor:
            valor = valor.replace('Acima de R$', '').replace(',', '').strip()
            return f'Acima de R${float(valor)}'
        elif 'até' in valor:
            valores = valor.split(' até R$')
            valor_min = float(valores[0].replace('R$', '').replace(',', '').strip())
            valor_max = float(valores[1].replace('R$', '').replace(',', '').strip())
            return f'R${int(valor_min)} até R${int(valor_max)}'
        else:
            return valor  # Retorna o valor original se não for possível converter
    except ValueError as e:
        print(f"Erro ao converter: {e}")
        return None 





# Carregar os dados
data = pd.read_csv('consumo de energia .csv', sep=',')

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mysql'
)
cursor = conexao.cursor()

# Nome da tabela onde os dados serão inseridos
nome_tabela = 'Projeto_LessEnergyA3_'

# Criar a tabela, se não existir (movido para depois da conexão)
create_table_query = '''
    CREATE TABLE IF NOT EXISTS Projeto_LessEnergyA3_ (
        Cidade VARCHAR(255),
        Região VARCHAR(255),
        TipoResidencia VARCHAR(255),
        NumPessoas INT,
        NumDispositivosEletronicos INT,
        EnergiaAlternativa VARCHAR(255),
        AutomacaoResidencial VARCHAR(255),
        EsforcoEconomizar VARCHAR(255),
        GastoMensalLuz VARCHAR(255),  
        ProvedorEnergia VARCHAR(255),
        ContaLuzCara VARCHAR(255)
    )
'''

cursor.execute(create_table_query)

# Modificar a coluna NumPessoas após a criação da tabela
alter_table_query = '''
    ALTER TABLE Projeto_LessEnergyA3_ MODIFY COLUMN NumPessoas VARCHAR(50)
'''

cursor.execute(alter_table_query)

# Inserção dos dados na tabela do banco de dados
for _, row in data.iterrows():
    try:
        # Convertendo 'GastoMensalLuz' para valor numérico
        gasto_mensal = convert_gasto_mensal(row['GastoMensalLuz'])

        # Convertendo 'NumDispositivosEletronicos' para um valor numérico representando a média do intervalo
        dispositivos_eletronicos = None

        intervalo = row['NumDispositivosEletronicos']
        if 'até' in intervalo:
            numeros = intervalo.split(' até ')
            valor_min = int(numeros[0])
            valor_max = int(numeros[1].split()[0])
            dispositivos_eletronicos = (valor_min + valor_max) // 2
        elif intervalo != 'Acima de 30 Eletrônicos':
            dispositivos_eletronicos = int(intervalo)

        # Ajuste para corresponder às colunas da tabela no banco de dados
        if dispositivos_eletronicos is not None:
            insert_query = f'''
                INSERT INTO {nome_tabela} (Cidade, Região, TipoResidencia, NumPessoas, NumDispositivosEletronicos,
                EnergiaAlternativa, AutomacaoResidencial, EsforcoEconomizar, GastoMensalLuz, ProvedorEnergia, ContaLuzCara)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            # Ajuste para corresponder aos valores das colunas
            values = (
                row['Cidade'], row['Região'], row['TipoResidencia'], row['NumPessoas'], dispositivos_eletronicos,
                row['EnergiaAlternativa'], row['AutomacaoResidencial'], row['EsforcoEconomizar'], gasto_mensal,
                row['ProvedorEnergia'], row['ContaLuzCara']
            )

            cursor.execute(insert_query, values)
   
    except Exception as e:
        print(f"Ocorreu um erro ao inserir na linha {_+1}: {e}")

# Confirma e fecha a conexão com o banco de dados
conexao.commit()
conexao.close()
print(data['GastoMensalLuz'].unique())
