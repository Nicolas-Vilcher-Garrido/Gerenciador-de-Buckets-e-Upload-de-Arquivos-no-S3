Este código Python foi desenvolvido para interagir com o Amazon S3, utilizando o módulo boto3. Ele oferece funcionalidades como:

Listagem de Buckets: O script lista todos os buckets que o usuário tem na sua conta AWS.
Criação de Buckets: Ele permite que o usuário crie um novo bucket, verificando previamente se o nome já está em uso. A criação é feita na região especificada (por padrão, us-east-2).
Upload de Arquivos: O código solicita ao usuário o caminho de um arquivo local e realiza o upload deste arquivo para o bucket S3 escolhido.
Listagem de Arquivos no Bucket: Após o upload, o script lista todos os arquivos presentes no bucket, garantindo que eles não sejam listados duas vezes (mesmo em buckets com múltiplas páginas de arquivos).
