from model import Product

class Storage:
    stor:list[Product]=[Product('P001','Hp Laser',9000)]

    @staticmethod
    def add(product:Product)->bool:
        Storage.stor.append(product)
        return True
    
    @staticmethod
    def list()->list[Product]:
        return Storage.stor
    
    @staticmethod
    def search(ref:str)->Product:
        for product in Storage.stor:
            if product.ref == ref:
                return product
        return None     
    
if __name__ == "__main__":
    printer:Product=Product('p001','Hp Laser',9000)
    lapop:Product=Product('p002','Dell p5',12000)

    Storage.add(printer)
    Storage.add(lapop)
    Storage.list()