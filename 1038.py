Item, Quantidade = map(float, input().split(' '))

if (Item == 1):
    PrecoTotal = 4.00 * Quantidade
elif (Item == 2):
    PrecoTotal = 4.50 * Quantidade
elif (Item == 3):
    PrecoTotal = 5.00 * Quantidade
elif (Item == 4):
    PrecoTotal = 2.00 * Quantidade
elif (Item == 5):
    PrecoTotal = 1.50 * Quantidade

print(f"Total: R$ {PrecoTotal:.2f}")