import re
from PyPDF2 import PdfReader

def extract_structure_from_decree(portaria_path):
    text = ""
    with open(portaria_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()

    # Expressão regular para extrair secretarias e departamentos
    secretarias = re.findall(r"Secretaria (de [A-Z][\w\s]+)", text)
    departamentos = re.findall(r"Departamento (de [A-Z][\w\s]+)", text)
    
    return secretarias, departamentos

def select_department():
    # Caminho da portaria configurado em config.py
    from config import portaria_file_path

    # Extração das secretarias e departamentos
    secretarias, departamentos = extract_structure_from_decree(portaria_file_path)

    print("Secretarias disponíveis:")
    for idx, sec in enumerate(secretarias, 1):
        print(f"{idx}. {sec}")
    
    # Selecionar secretaria
    sec_choice = int(input("Selecione o número da Secretaria: "))
    selected_secretaria = secretarias[sec_choice - 1]

    print("\nDepartamentos disponíveis:")
    for idx, dep in enumerate(departamentos, 1):
        print(f"{idx}. {dep}")

    # Selecionar departamento
    dep_choice = int(input("Selecione o número do Departamento: "))
    selected_departamento = departamentos[dep_choice - 1]

    return selected_secretaria, selected_departamento

