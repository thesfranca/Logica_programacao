print("---CALCULADORA DE RESISTÊNCIA MECÂNICA---")

print("1 - Tensão Normal")
print("2 - Cisalhamento")

op = input("Escolha o tipo de análise: ")

# --- SEÇÃO: ESCOLHA DE MATERIAL ---
print("\n--- ESCOLHA DO MATERIAL ---")
print("1 - Aço Carbono (Limite aprox. 250 MPa)")
print("2 - Alumínio (Limite aprox. 275 MPa)")
print("3 - Material Cerâmico (Limite aprox. 300 MPa)")
print("4 - Outro (Inserir limite manualmente)")

escolha_mat = input("Escolha o material: ")

# Definindo o limite automaticamente com base na escolha
if escolha_mat == "1":
    limite = 250000000.0  # 250 milhões de Pa (250 MPa)
    nome_mat = "Aço Carbono"
elif escolha_mat == "2":
    limite = 275000000.0  # 275 milhões de Pa (275 MPa)
    nome_mat = "Alumínio"
elif escolha_mat == "3":
    limite = 300000000.0  # 300 milhões de Pa (300 MPa)
    nome_mat = "Material Cerâmico"
else:
    # Caso escolha 4 ou digite errado, pede o valor manualmente
    limite = float(input("Limite do material (Pa): "))
    nome_mat = "Personalizado"


# --- NOVA SEÇÃO: UNIDADE DE FORÇA E CONVERSÃO ---
print("\n--- UNIDADE DE FORÇA ---")
print("1 - Newton (N)")
print("2 - Quilograma-força (kgf)")
unidade_f = input("Escolha a unidade da força: ")

# Fator de conversão constante da gravidade
FATOR_CONVERSAO = 9.80665 

if unidade_f == "2":
    F_kgf = float(input("\nForça (kgf): "))
    F_N = F_kgf * FATOR_CONVERSAO # Converte kgf para Newton
else:
    # Se escolher 1 ou qualquer outra coisa, assume Newton como padrão
    F_N = float(input("\nForça (N): "))
    F_kgf = F_N / FATOR_CONVERSAO # Converte Newton para kgf
# ------------------------------------------------


# Entrada da Área

A = float(input("Área (m²): "))

# Cálculo da tensão (Atenção: A fórmula Pa = N / m² exige Força em Newtons)
tensao = F_N / A
print(f"\nTensão na peça: {tensao/1e6:.2f} MPa")

# Cálculo do fator de segurança
fs = limite / tensao

# Define o tipo de análise
if op == "1":
    tipo = "Tensão Normal"
else:
    tipo = "Tensão de Cisalhamento"

# Resultados
print("\n--- RESULTADO ---")
print("Tipo da análise:", tipo)
print("Material analisado:", nome_mat)
print(f"Força Aplicada: {F_N:.2f} N  |  {F_kgf:.2f} kgf") # Exibe ambas as unidades
print(f"Tensão: {tensao:.2f} Pa")
print(f"Limite do material: {limite:.2f} Pa")
print(f"Fator de Segurança: {fs:.2f}")

# Verificação do limite de escoamento
if tensao < limite:
    print("✅ Material seguro (não atingiu o limite de escoamento/falha)")
elif tensao == limite:
    print("⚠️ Material no limite de escoamento/falha")
else:
    print("❌ Material entrou em escoamento ou falhou")