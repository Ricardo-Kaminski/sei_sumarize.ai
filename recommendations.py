def generate_recommendations(summary, department_info, coordination_info):
    # Personalize recomendações com base no resumo e nas funções extraídas da portaria
    recommendations = []
    
    if "financiamento" in summary and "financiamento" in department_info["funcoes"]:
        recommendations.append("Escrever uma nota técnica sobre o financiamento.")
    
    if "despacho" in summary and "despacho" in department_info["funcoes"]:
        recommendations.append("Analisar o despacho mais recente e encaminhar para a coordenação.")

    # Adicionar mais regras de recomendação
    return recommendations

