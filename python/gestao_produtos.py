"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Lista o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3

################################################################################
##
##       PRODUTOS E CATÁLOGO
##
################################################################################

PRODUCT_TYPES = {
    'AL': 'Alimentação',
    'DL': 'Detergente p/ Loiça',
    'FRL': 'Frutas e Legumes'
}

# id    : > 0 e tem que ter cinco digitos
# nome
# tipo
# quantidade
# preco

class Produto:
    def __init__(
            self, 
            id_: int, 
            nome: str, 
            tipo: str, 
            quantidade: int,
            preco: dec,
    ):
        if id_ < 0 or len(str(id_)) != 5:
            raise InvalidProdAttribute(f'{id_=} inválido (deve ser > 0 e ter 5 dígitos)')
        if not nome:
            raise InvalidProdAttribute('Nome vazio')
        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttribute(f'Tipo de produto ({tipo}) desconhecido')
        if quantidade < 0:
            raise InvalidProdAttribute('Quantidade deve ser >= 0')
        if preco < 0:
            raise InvalidProdAttribute('Preço deve ser >= 0')

        self.id = id_
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco
    #:

    @classmethod
    def from_csv(cls, line: str, delim = CSV_DEFAULT_DELIM) -> 'Produto':
        attrs = line.split(delim)
        return cls(
                id_ = int(attrs[0]),
                nome = attrs[1],
                tipo = attrs[2],
                quantidade = int(attrs[3]),
                preco = dec(attrs[4])
            )
    #:

    @property # criando atributo computado
    def get_desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.tipo]
    #:

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[id_= {self.id}  nome = "{self.nome}" tipo = "{self.tipo}"]'
    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return (f'{cls_name}(id_ = {self.id} nome = {self.nome} tipo={self.tipo} '
                f'quantidade = {self.quantidade} preço = {repr(self.preco)}')
    #:

    def com_iva(self, taxa_iva: dec) -> dec:
        return self.preco * (1 + taxa_iva / 100)
    #:
#:

# class ProdutoEspecial(Produto):
#     def __init__(self, promocao, *args, **kargs):
#         super().__init__(*args, **kargs)
#         self.promocao = promocao
#     #:

#     def valor_stock(self) -> dec:
#         return self.quantidade * self.preco;
#     #:
# #:

class InvalidProdAttribute(ValueError):
    pass
#:

class CatalogoProdutos:
    def __init__(self):
        self._prods = {}
    #:

    def append(self, prod: Produto) -> None:
        if prod.id in self._prods:
            raise DuplicateValue(f'Produt com id {prod.id} já existente.')
        self._prods[prod.id] = prod;
    #:

    def _dump(self):
        for prod in self._prods.values():
            print(prod)
        #:
    #:

    def get_by_id(self, id: int) -> Produto | None:
        return self._prods.get(id)
    #:

    def pesquisa(self, criterio) -> 'CatalogoProdutos':
        encontrados = CatalogoProdutos()
        for prod in self._prods.values():
            if criterio(prod):
                encontrados.append(prod)
        return encontrados
    #:

    def remove_por_id(self, id: int) -> Produto | None:
        prod = self._prods.get(id)
        if prod:
            del self._prods[id]
        return prod
    #:

    def remove(self, criterio) -> 'CatalogoProdutos':
        a_remover = self.pesquisa(criterio)
        for prod in a_remover:
            del self._prods[prod.id]
        return a_remover
    #:

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}[#produtos = {len(self._prods)}]'
    #:

    def __iter__(self):
        for prod in self._prods.values():
            yield prod
        #:
    #:

    def __len__(self):
        return len(self._prods)
    #:
#:

class DuplicateValue(Exception):
    pass
#:

################################################################################
##
##       LEITURA DOS FICHEIROS
##
################################################################################

def le_produtos(caminho_fich: str, delim = CSV_DEFAULT_DELIM) -> CatalogoProdutos:
    prods = CatalogoProdutos()
    with open(caminho_fich, 'rt') as file:
        for line in linhas_relevantes(file):
            prods.append(Produto.from_csv(line, delim))
    return prods
#:

def linhas_relevantes(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        yield line


################################################################################
##
##       MENU, OPÇÕES E INTERAÇÃO COM O UTILIZADOR
##
################################################################################

def exibe_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent - 1), *args, **kargs)
#:

def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
    #:
#:

def pause(msg: str = 'Pressione ENTER para continuar...', indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")
#:

produtos : CatalogoProdutos | None = None

def entrada(msg: str, indent = DEFAULT_INDENTATION) -> str:
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")

def exec_listar():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}'
    # separador =  '|'.join(['-' * 16] * 5)
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for prod in produtos:
        linha = f'{prod.id:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}'
        exibe_msg(linha)
    #:
    exibe_msg(separador)
    print()
    pause()
#:

def exec_terminar():
    sys.exit(0)
#:

def exec_menu():
    """
    - Lista o catálogo
    - Pesquisar por alguns campos
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
    """

    while True:
        cls()
        exibe_msg("*******************************************")
        exibe_msg("* L - Listar catálogo                     *")
        exibe_msg("* P - Pesquisar por id                    *")
        exibe_msg("* A - Acrescentar produto                 *")
        exibe_msg("* E - Eliminar produto                    *")
        exibe_msg("* G - Guardar catálogo em ficheiro        *")
        exibe_msg("*                                         *")
        exibe_msg("* T - Terminar programa                   *")
        exibe_msg("*******************************************")

        print()
        opcao = entrada("OPCAO> ").strip().upper()

        if opcao in ('L', 'LISTAR'):
            exec_listar()
        elif opcao in ('T', 'TERMINAR'):
            exec_terminar()
        else:
            exibe_msg(f"Opção {opcao} inválida!")
            pause()
#:

def main() -> None:
    global produtos
    produtos = le_produtos('produtos.csv')
    exec_menu()
#:

if __name__ == '__main__':
    main()
#: