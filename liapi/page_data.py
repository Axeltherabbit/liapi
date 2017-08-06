class page_data(dict):
    def __init__(self,j):
        content=["currentPage","maxPerPage","nbResults","previousPage","nextPage","nbPages"]
        for i in content:
            try:
                self.__dict__[i]=j[i]
            except:
                self.__dict__[i]=None
