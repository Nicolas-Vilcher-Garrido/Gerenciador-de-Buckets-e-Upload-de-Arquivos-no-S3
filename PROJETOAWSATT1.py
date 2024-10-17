import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Cria uma sessão com s3

s3 = boto3.client('s3')


# Listar todos os buckets

def list_buckets():
    try:
        response = s3.list_buckets()
        print('Buckets existentes: ')
        for bucket in response['Buckets']:
            print(f'{bucket["Name"]}')
        return [bucket['Name'] for bucket  in response['Buckets']]
    except ClientError as e:
        print('Erro ao listar os buckets: {e}')
        return []
    
# Função Criar bucket (No meu caso está na região us-east-2)

def create_bucket(bucket_name, region='us-east-2'):
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
        print(f'Bucket {bucket_name} criado com sucesso!')
    
    except ClientError as e:
        print(f'Erro ao criar Bucket {e}')
        
# Função para upload de um arquivo 

def upload_file(file_path, bucket_name, file_key):
    try:
        s3.upload_file(file_path, bucket_name, file_key)
        print(f'Arquivo "{file_key}" enviado para o bucket "{bucket_name}"')
    except NoCredentialsError:
        print('Erro: Credenciais AWS não encontradas')
    except ClientError as e:
        print(f' Erro ao enviar o arquivo: {e}')

# Função listar arquivos no bucket

def list_bucket_file(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        print(f'Arquivo  no Bucket "{response}":')
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f'{obj["Key"]}:')
        else:
            print('Nenhum arquivo encontrado  no bucket')
    except ClientError as e:
        print(f'Erro ao listar arquivos: {e}')

# Lista buckets existentes

if __name__ == '__main__':
    existing_buckets = list_buckets()
    
# Solicita o nome do novo bucket
bucket_name = input('Digite o nome do novo Bucket a ser criado: ')

# Verifica se o Bucket ja existe
if bucket_name in existing_buckets:
    print(f'O Bucket {bucket_name} lá existe')
else:
    # Cria um novo bucket se ele não existir
    create_bucket(bucket_name)
    
# Solicita o caminho do arquivo a ser enviado

file_path = input('Digite o caminho completo do arquivo que deseja enviar: ')
file_key = file_path.split('/')[-1] # Extrai apenas o nome do arquivo ao invés do caminho todo
upload_file(file_path, bucket_name, file_key)

# Lista os arquivos no bucket
list_buckets(bucket_name)

        
        
