N1, N2, N3, N4 = map(float, input().split(' '))

Media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / (2 + 3 + 4 + 1)
print(f'Media: {Media:.1f}')

if Media >= 7:
    print('Aluno aprovado.')
elif Media >= 5:
    print('Aluno em exame.')

    NotaExame = float(input())
    print("Nota do exame: {:.1f}".format(NotaExame)) # é usado em estrutura de repetição, substituindo o f no coemço para esse format
    Media = (Media + NotaExame) / 2

    if Media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f"Media final: {Media:.1f}")

else:
    print('Aluno reprovado.')