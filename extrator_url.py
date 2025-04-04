import re 

# Classe responsável por manipular e extrair informações de uma URL
class ExtratorURL:
    def __init__(self, url):
        # Inicializa o objeto com a URL sanitizada e valida a URL
        self.__url = self.sanitiza_url(url)
        self.valida_url()

    # Método para remover espaços em branco da URL ou retornar uma string vazia se o tipo for inválido
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    # Método para validar a URL utilizando uma expressão regular
    def valida_url(self):
        if not self.__url:
            # Lança um erro se a URL estiver vazia
            raise ValueError('A URL está vazia')
        
        # Regex para validar URLs genéricas (http, https, com ou sem "www")
        padrao_url = re.compile(r'^(http(s)?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$')
        match = padrao_url.match(self.__url)

        if not match:
            # Lança um erro se a URL não for válida
            raise ValueError('A URL não é válida')
    
    # Propriedade para acessar a URL armazenada
    @property
    def url(self):
        return self.__url
                
    # Método para obter a parte base da URL (antes do '?')
    def get_url_base(self):
        indice_interrogacao = self.__url.find('?')
        url_base = self.__url[:indice_interrogacao]
        return url_base
    
    # Método para obter os parâmetros da URL (após o '?')
    def get_url_parametros(self):
        indice_interrogacao = self.__url.find('?')
        url_parametros = self.__url[indice_interrogacao+1:]
        return url_parametros
    
    # Método para obter o valor de um parâmetro específico na URL
    def get_valor_parametro(self, nome_parametro):
        # Encontra o índice do parâmetro na string de parâmetros
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        if indice_parametro == -1:
            # Retorna uma string vazia se o parâmetro não for encontrado
            return '\n'
        
        # Calcula o índice do valor do parâmetro
        indice_valor = indice_parametro + len(nome_parametro) + 1
        # Encontra o próximo '&' para delimitar o valor do parâmetro
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            # Se não houver '&', o valor vai até o final da string
            valor = self.get_url_parametros()[indice_valor:]
        else:
            # Caso contrário, o valor vai até o próximo '&'
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.__url)
    
    def __str__(self):
        return f'''URL: {self.__url}
Parâmetros: {self.get_url_parametros()}
URL Base: {self.get_url_base()}'''
    
    def __eq__(self, value):
        return self.__url == value.url


