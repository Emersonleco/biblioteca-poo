from livro.livro import Livro


class LivroFisico(Livro):
    def __init__(self, livro_id, autor, titulo, ano_publi, num_pag):
        super().__init__(livro_id, autor, titulo, ano_publi)
        self.__num_pag = num_pag

    @property
    def num_pag(self):
        return self.__num_pag

    @num_pag.setter
    def num_pag(self, value):
        self.__num_pag = value


