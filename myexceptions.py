class Error(Exception):
    "Base class for other exceptions"
    def __init__(self, message):
        super().__init__(message)

class InvalidProdIDException(Error):
    def __init__(self, prodId, message="Product is not in (1, 25) range"):
        self.prodId = prodId
        self.message = message
        super().__init__(self.message)

class InvalidStoreIDException(Error):
    def __init__(self, storeId, message="Store Id is not in (1, 4) range"):
        self.storeId = storeId
        self.message = message
        super().__init__(self.message)