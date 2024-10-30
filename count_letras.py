def count_letter_a(s):
    # Converte a string para minúsculas para facilitar a contagem
    s_lower = s.lower()
    count = s_lower.count('a')  # Conta quantas vezes 'a' aparece na string
    return count

def main():
    # Lista de strings de teste
    test_strings = [
        "Alguém ama a arte",
        "Apenas um teste",
        "Não há letras aqui",
        "Essa frase não tem a letra procurada",
        "Outra linha sem a",
        "A letra 'a' aparece várias vezes: aaaa",
        "Nada a declarar",
        "Python é incrível!"
    ]
    
    for text in test_strings:
        # Conta a letra 'a'
        count = count_letter_a(text)
        
        if count > 0:
            print(f"A letra 'a' (maiúscula ou minúscula) aparece {count} vez(es) na string: \"{text}\"")
        else:
            print(f"A letra 'a' (maiúscula ou minúscula) não está presente na string: \"{text}\"")

if __name__ == "__main__":
    main()
