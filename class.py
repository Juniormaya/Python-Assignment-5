class smartphone:
    def __init__(self, brand, model, storage, ram):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.ram = ram

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.ram}GB RAM"

    def __repr__(self):
        return f"smartphone(brand='{self.brand}', model='{self.model}', storage={self.storage}, ram={self.ram})"
    
    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo!"
    
# inheritance
class smartphone_with_camera(smartphone):
    def __init__(self, brand, model, storage, ram, camera_megapixels):
        super().__init__(brand, model, storage, ram)
        self.camera_megapixels = camera_megapixels

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, {self.ram}GB RAM and {self.camera_megapixels}MP camera"

    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo with {self.camera_megapixels}MP camera!"