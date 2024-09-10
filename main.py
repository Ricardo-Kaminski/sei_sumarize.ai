from extractor import list_process_files, extract_zip_files
from pdf_reader import process_pdfs
from summarizer import summarize_text
from recommendations import generate_recommendations
from portaria_reader import select_department
import config

def main():
    # Diretório dos arquivos de processos ZIP
    process_directory = "/mnt/data/Processos"
    
    # Listar os arquivos de processos e permitir seleção
    selected_zip_file = list_process_files(process_directory)
    
    if selected_zip_file:
        # Extrair os arquivos do processo
        process_number, document_count_by_type = extract_zip_files(selected_zip_file)

        # Exibir as informações do processo
        print(f"Número do Processo: {process_number}")
        print("Quantidade de documentos por tipo:")
        for doc_type, count in document_count_by_type.items():
            print(f"{doc_type}: {count}")

        # Continuar com o processamento dos PDFs
        extracted_files = process_pdfs(selected_zip_file)

        # Gerar resumos e recomendações
        for file_name, text in extracted_files.items():
            summary = summarize_text(text)
            department_info, coordination_info = select_department()
            recommendations = generate_recommendations(summary, department_info, coordination_info)
            print(f"Arquivo: {file_name}")
            print(f"Resumo: {summary}")
            print(f"Recomendações: {recommendations}")
            print("----------")

if __name__ == "__main__":
    main()
