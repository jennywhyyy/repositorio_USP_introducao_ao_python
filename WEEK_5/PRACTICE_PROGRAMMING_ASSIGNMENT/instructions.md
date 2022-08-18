Nesta lista de exercícios vamos praticar os conceitos vistos até agora.  Cada exercício deve ser resolvido em um arquivo separado e a seguir  enviado através da web. A correção automática pode demorar alguns  minutos. Você pode submeter a mesma resposta mais de uma vez caso  perceba que a resposta anterior tinha algum problema; a última versão é a  que vale.

Seja preciso quando valores de retorno pedidos forem cadeias de caracteres.



Exercício 1 - FizzBuzz
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

	'Fizz' se o número for divisível por 3 e não for divisível por 5;

	'Buzz' se o número for divisível por 5 e não for divisível por 3;

	'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Exemplos de execução no Python Shell

	>>>fizzbuzz(3)
	"Fizz"
	>>>fizzbuzz(5)
	"Buzz"
	>>>fizzbuzz(15)
	"FizzBuzz"
	>>>fizzbuzz(4)
	4
As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas



Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

Exemplos de execução no Python Shell

	>>>maximo(30, 14, 10)
	30
	>>>maximo(0, -1, 1)
	1
