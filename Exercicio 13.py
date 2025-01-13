w = [['Joao', 10], ['Maria', 19], ['Jose', 12], ['João', 19]]

def nomes(w):
    maior = w[0][1] #o maior na primeira iteração é o primeiro aluno da lista
    nomes = [] #lista para armazenar os nomes dos alunos com a maior nota
    for i in range(len(w)): #percorre a lista de alunos. O range é o tamanho da lista para que o loop percorra todos os alunos
        if w[i][1] > maior: #se a nota do aluno atual for maior que a maior nota até o momento, este loop só serve para encontrar a maior nota da lista, se houver outras notas terão de ser iguais e isso será tratado no segundo loop
            maior = w[i][1] #a maior nota passa a ser a nota do aluno atual
    for i in range(len(w)): #percorre a lista de alunos novamente, o segundo loop é necessário porque o primeiro loop já encontrou a maior nota e este só serve para encontrar alunos com a mesma nota
        if w[i][1] == maior: 
            nomes.append(w[i][0]) #adiciona o nome do aluno à lista de nomes
    return nomes

print(nomes(w))