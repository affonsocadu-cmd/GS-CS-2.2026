def ler_entrada(pergunta):
    while True:
        valor = input(f"{pergunta} (1 = Sim / 0 = Nao): ").strip()
        if valor in ("0", "1"):
            return int(valor)
        print("Entrada invalida! Digite apenas 1 ou 0.\n")

def avaliar_original(a, b, c):
    # S = A.!B.C + A.B.!C + A.B.C
    return int((a and not b and c) or (a and b and not c) or (a and b and c))

def avaliar_simplificada(a, b, c):
    # S = A . (B + C)
    return int(a and (b or c))

def validar_tabela_verdade():
    print("\n--- VALIDACAO DA TABELA-VERDADE (8 COMBINACOES) ---")
    print("A | B | C || Original | Simplificada | Status")
    print("-" * 47)
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                orig = avaliar_original(a, b, c)
                simp = avaliar_simplificada(a, b, c)
                status = "OK" if orig == simp else "ERRO"
                print(f"{a} | {b} | {c} ||    {orig}     |      {simp}       | {status}")

def main():
    print("=== ASSISTENTE DE TRIAGEM - 1a HABILITACAO ===")
    a = ler_entrada("O candidato tem 18 anos ou mais?")
    b = ler_entrada("O candidato sabe ler e escrever?")
    c = ler_entrada("O candidato possui RG e CPF em maos?")

    resultado = avaliar_simplificada(a, b, c)

    print("\n--- ORIENTACAO AO USUARIO ---")
    if resultado == 1:
        print("[S = 1] Agendamento liberado para abertura de processo e exames.")
    else:
        print("[S = 0] Atendimento bloqueado. Verifique os requisitos minimos.")

    validar_tabela_verdade()

if __name__ == "__main__":
    main()
