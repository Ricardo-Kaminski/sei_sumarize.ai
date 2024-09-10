import zipfile
import os
import re
from collections import defaultdict

def list_process_files(process_directory):
    # Listar todos os arquivos ZIP na pasta "Processos"
    zip_files = [f for f in os.listdir(process_directory) if f.endswith(".zip")]
    
    if not zip_files:
        print("Nenhum arquivo de processo encontrado na pasta.")
        return None
    
    # Exibir os arquivos de processos para o usuário selecionar
    print("Processos disponíveis:")
    for idx, file in enumerate(zip_files, 1):
        print(f"{idx}. {file}")
    
    # Solicitar que o usuário selecione um processo
    choice = int(input("Selecione o número do processo que deseja resumir: "))
    selected_file = zip_files[choice - 1]
    
    return os.path.join(process_directory, selected_file)

def extract_zip_files(zip_file):
    # Extrair o número do processo a partir do nome do arquivo
    process_number = extract_process_number(zip_file)

    # Diretório de saída
    output_dir = f"/mnt/data/SEI_extracted/{process_number}"
    
    # Extrair arquivos
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        print(f"Arquivos extraídos para {output_dir}")
    
    # Contagem de documentos por tipo
    document_count_by_type = defaultdict(int)
    
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            document_type = identify_document_type(file)
            document_count_by_type[document_type] += 1

    return process_number, document_count_by_type

def identify_document_type(file_name):
    if re.search(r"(?i)despacho", file_name):
        return "Despacho"
    elif re.search(r"(?i)email", file_name):
        return "E-mail"
    elif re.search(r"(?i)nota.técnica", file_name):
        return "Nota Técnica"
    elif re.search(r"(?i)relatório", file_name):
        return "Relatório"
    elif re.search(r"(?i)ofício", file_name):
        return "Ofício"
    else:
        return "Outro"

def extract_process_number(zip_file_name):
    # Expressão regular para extrair o número do processo do nome do arquivo
    match = re.search(r"SEI_(\d+)_", zip_file_name)
    if match:
        return match.group(1)
    else:
        raise ValueError("Número do processo não encontrado no nome do arquivo")

# Exemplo de uso
process_directory = "/mnt/data/Processos"
selected_zip_file = list_process_files(process_directory)

if selected_zip_file:
    process_number, document_count_by_type = extract_zip_files(selected_zip_file)

    print(f"Número do Processo: {process_number}")
    print("Quantidade de documentos por tipo:")
    for doc_type, count in document_count_by_type.items():
        print(f"{doc_type}: {count}")
