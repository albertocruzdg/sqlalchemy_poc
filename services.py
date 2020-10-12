class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def get(self, id):
        return repository.get(id)

    def create(self, product):
        repository.create(product)

    def update(self, id, product):
        repository.update(id, product)

    def delete(self, id):
        repository.delete(id)

