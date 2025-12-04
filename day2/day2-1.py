def calcula_numero_de_casas(num) -> int:
    result = 0
    while num >= 1:
        num /= 10
        result += 1
    return result


def encontra_primeira_ocorrencia(num, i):
    result = int(num)
    if num[:int(i/2)] >= num[int(i/2):]:
        result = int(num[:int(i/2)] + num[:int(i/2)])
    else:
        result = int(num[:int(i/2)]) + 1
        result = int(str(result) + str(result))

    return result

with open("input.txt", "r") as file:
    content = file.read()

id_ranges = content.split(",")
sum_ids = 0

for id_range in id_ranges:
    a,b = id_range.split("-")
    tamanho_a = calcula_numero_de_casas(int(a))
    tamanho_b = calcula_numero_de_casas(int(b))

    for i in range(tamanho_a, tamanho_b + 1):
        if i % 2 == 0:
            if i == tamanho_a and i == tamanho_b:
                primeira_ocr = encontra_primeira_ocorrencia(a, i)

                for num in range(primeira_ocr, int(b)+1, 10**(int(tamanho_a/2)) + 1 ):
                    sum_ids += num

            elif i == tamanho_a:
                primeira_ocr = encontra_primeira_ocorrencia(a, i)

                for num in range(primeira_ocr, 10**tamanho_a, 10**(int(tamanho_a/2)) + 1 ):
                    sum_ids += num

            elif i == tamanho_b:
                primeira_ocr = encontra_primeira_ocorrencia(str(10**(tamanho_b - 1)), i)
                for num in range(primeira_ocr, int(b)+1, 10**(int(tamanho_b/2)) + 1 ):
                    sum_ids += num


            else:
                primeira_ocr = encontra_primeira_ocorrencia(str(10**(i-1)), i)
                for num in range (primeira_ocr, 10**i, 10**int(i/2) + 1):
                    sum_ids += num


print(sum_ids)
