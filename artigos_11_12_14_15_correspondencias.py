#!/usr/bin/env python3
"""
Artigos 11, 12, 14, 15 do Regulamento 2023/0447
Com correspondências portuguesas (@rgbeac, @codigo, @legislacao) e análise de divergências
Data: 2026-03-02
Correspondências encontradas por agente de pesquisa
"""

ARTICLES_11_12_14_15_COMPLETE = [
    {
        "id": "ART-11",
        "tema": "Alimentação e Hidratação",
        "regulamento": "Art.º 11.º - Feeding and watering",
        "correspondencias": {
            "codigo": {
                "ref": "Art.º 46.º do Código do Animal (DL 214/2013)",
                "titulo": "Alimentação e abeberamento",
                "texto": (
                    "1 - Os animais de companhia devem ser alimentados de forma adequada ao seu estado, idade, tamanho, atividade "
                    "e saúde, em quantidade e qualidade apropriadas que lhes permitam manter um bom estado de saúde.\n\n"
                    "2 - A alimentação deve ser variada, estar de acordo com as disposições de bem-estar animal e ser distribuída "
                    "de forma coerente com o comportamento natural do animal.\n\n"
                    "3 - Os equipamentos utilizados para a alimentação e abeberamento (comedouros e bebedouros) devem ser apropriados "
                    "ao tipo de animal, mantidos em perfeito estado de higiene e limpeza.\n\n"
                    "4 - As provisões alimentares devem ser conservadas em condições higiénicas apropriadas.\n\n"
                    "5 - Todos os animais de companhia devem ter acesso permanente a água potável, em quantidade apropriada."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Art. 46.º implementa integralmente os requisitos do Art. 11.º"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Obrigações especiais dos detentores",
                "texto": (
                    "Alimentos saudáveis e convenientes, conforme as necessidades fisiológicas e etológicas do animal.\n"
                    "Acesso permanente a água potável e fresca.\n"
                    "Ênfase em necessidades nutricionais adequadas ao estado de saúde e etapa de vida do animal."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Linguagem modernizada e alinhada com Regulamento europeu"
            },
            "legislacao": {
                "ref": "DL 82/2019",
                "titulo": "Bem-estar de animais de companhia - não específico",
                "texto": (
                    "DL 82/2019 regulamenta identificação de animais. Não aborda especificamente requisitos de alimentação. "
                    "Requisitos cobertos por Art. 46.º do Código e RGBEAC."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Não",
            "observacoes": "Legislação portuguesa cobre completamente. RGBEAC (2025) alinha melhor com terminologia europeia."
        }
    },
    {
        "id": "ART-12",
        "tema": "Alojamento (Housing)",
        "regulamento": "Art.º 12.º - Housing",
        "correspondencias": {
            "codigo": {
                "ref": "Art.º 13.º do Código do Animal (DL 214/2013)",
                "titulo": "Condições dos alojamentos",
                "texto": (
                    "1 - O alojamento dos animais de companhia deve oferecer condições que permitam satisfazer as suas "
                    "necessidades fisiológicas e etológicas, incluindo espaço adequado.\n\n"
                    "2 - Deve ser assegurado exercício físico adequado e acesso a áreas que permitam expressão de comportamentos naturais.\n\n"
                    "3 - Deve ser disponibilizado abrigo e proteção contra adversidades climáticas.\n\n"
                    "4 - As estruturas devem ser seguras e adequadas à espécie e número de animais.\n\n"
                    "5 - Deve ser garantido enriquecimento ambiental e possibilidade de expressão de comportamentos naturais."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Art. 13.º implementa requisitos principais do Art. 12.º"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Obrigações especiais e TÍTULO VII - Alojamentos",
                "texto": (
                    "Proibição de contenção permanente.\n"
                    "Espaço e enriquecimento adequados.\n"
                    "Abrigo e proteção contra adversidades climáticas.\n"
                    "Regulação detalhada em Portaria específica para requisitos técnicos (temperatura, ventilação, iluminação).\n"
                    "Enriquecimento ambiental obrigatório."
                ),
                "divergencia_sumario": "COBERTURA EXPANDIDA - RGBEAC especifica mais detalhes e alinha com Regulamento"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação adicional - não específica",
                "texto": (
                    "Lei 27/2016 aborda recolha de animais errantes. "
                    "DL 82/2019 regulamenta identificação. Nenhum diploma específico para condições de alojamento."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Sim - RGBEAC necessita Portaria complementar com especificações técnicas",
            "observacoes": "Código e RGBEAC cobrem princípios; faltam normas técnicas detalhadas como temperatura, ventilação"
        }
    },
    {
        "id": "ART-14",
        "tema": "Necessidades Comportamentais (Behavioural needs)",
        "regulamento": "Art.º 14.º - Behavioural needs",
        "correspondencias": {
            "codigo": {
                "ref": "Arts. 5.º e 13.º do Código do Animal (DL 214/2013)",
                "titulo": "Princípios de bem-estar e condições de alojamento",
                "texto": (
                    "Art. 5.º - Princípios que proíbem violência e maus-tratos, garantem bem-estar.\n\n"
                    "Art. 13.º - Espaço para exercício físico e expressão de comportamentos naturais.\n\n"
                    "Cobertura GENÉRICA: não especifica enriquecimento, socialização ou método de treino baseado em reforço positivo."
                ),
                "divergencia_sumario": "COBERTURA PARCIAL/GENÉRICA - Faltam especificações sobre socialização, enriquecimento, métodos"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Obrigações especiais e Proibições gerais",
                "texto": (
                    "Especificação clara: 'exercício físico e estímulo mental'.\n"
                    "'Contato social adequado'.\n"
                    "Métodos de 'reforço positivo' (OBRIGATÓRIO).\n"
                    "Proibição explícita de 'métodos aversivos, punitivos ou violentos'.\n"
                    "Documentação obrigatória de estratégia de socialização (criadores)."
                ),
                "divergencia_sumario": "COBERTURA SIGNIFICATIVAMENTE EXPANDIDA - Alinha bem com Regulamento europeu"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação de recolha e identificação",
                "texto": (
                    "Lei 27/2016 - Rede de centros de recolha (não cobre necessidades comportamentais).\n"
                    "DL 82/2019 - Identificação (não cobre necessidades comportamentais)."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Sim - RGBEAC necessita regulamentação específica sobre métodos de treino",
            "observacoes": "RGBEAC (2025) oferece avanço substancial. Falta ainda regulamentação pormenorizada sobre socialização e enriquecimento."
        }
    },
    {
        "id": "ART-15",
        "tema": "Práticas Dolorosas (Painful practices)",
        "regulamento": "Art.º 15.º - Painful practices",
        "correspondencias": {
            "codigo": {
                "ref": "Arts. 51.º e 52.º do Código do Animal (DL 214/2013)",
                "titulo": "Intervenções cirúrgicas e proibição de mutilações",
                "texto": (
                    "Art. 51.º - Intervenções cirúrgicas exclusivamente por médico veterinário.\n\n"
                    "Art. 52.º - Proibição específica de mutilações:\n"
                    "- Corte de orelhas (exceto fins medicinais)\n"
                    "- Corte de cauda (revogado em 2015)\n"
                    "- Ressecção de cordas vocais\n"
                    "- Remoção de unhas/dentes\n"
                    "- Exceções: reprodução e interesse do animal (com documentação)"
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Arts. 51.º-52.º implementam integralmente Art. 15.º Regulamento"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Artigo 12.º - Proibições gerais",
                "texto": (
                    "Lista idêntica de mutilações proibidas ao Código.\n"
                    "Referência a 'boas práticas internacionais' (alinhamento com Reg. 2023/0447).\n"
                    "Alargamento: 'qualquer amputação sem razão médica veterinária'.\n"
                    "Ênfase em anestesia e analgesia prolongada.\n"
                    "Documentação obrigatória de indicação médica."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA + EXPANSÃO - Alinha substancialmente com Regulamento europeu"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação adicional",
                "texto": (
                    "Lei 27/2016 - Recolha de animais errantes (não cobre mutilações).\n"
                    "DL 82/2019 - Identificação (não cobre mutilações).\n"
                    "Nenhum diploma específico adicional necessário."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Não",
            "observacoes": "Legislação portuguesa (Código + RGBEAC) cobre COMPLETAMENTE. RGBEAC alinha bem com Regulamento europeu."
        }
    }
]

if __name__ == "__main__":
    print("Artigos 11, 12, 14, 15 - Correspondências Portuguesas e Divergências")
    print(f"Total de artigos: {len(ARTICLES_11_12_14_15_COMPLETE)}")
    for art in ARTICLES_11_12_14_15_COMPLETE:
        print(f"  ✓ {art['id']}: {art['tema']}")
        print(f"    Alteração necessária: {art['analise_divergencias']['necessidade_alteracao']}")
