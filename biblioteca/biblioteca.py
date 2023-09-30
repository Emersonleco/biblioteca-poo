from livro.livro_fisico import LivroFisico
from membro.membro import Membro

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        self.__membros.append(membro)
        print("Novo membro adicionado!")

    def deletarMembro(self, membro_id):
        for membro in self.__membros:
            if membro.membro_id == membro_id:
                self.__membros.remove(membro)
                print("Membro deletado com sucesso!")

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print("Novo livro adicionado a biblioteca")

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.livro_id == id:
                self.__livros.remove(livro)
                print("Livro deletado com sucesso!")

    def listarLivros(self):
        for livro in self.__livros:
            print("---- Dados do Livro ----")
            print(f"ID: {livro.livro_id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano_publi}")
            print(f"Nº de páginas: {livro.num_pag} \n")

    def listarMembro(self):
        print("---- Membros Cadastrados ----")
        for membro in self.__membros:
            print(f"ID: {membro.membro_id}")
            print(f"Nome: {membro.nome}")
            print(f"Endereço: {membro.endereco}")
            print(f"Telefone: {membro.telefone}")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    m1 = Membro(1, "Luis", "Rua c", "88 8888-8888")
    m2 = Membro(2, "Cnpjoto", "Rua calabreso", "88 77777-7777")
    livro1 = LivroFisico(1, "Talkien", "LOR", 1970, 700)
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(livro1)
    biblioteca.listarMembro()
    biblioteca.listarLivros()