class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}. Must be one of {Pet.PET_TYPES}")
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Returns a list of pets the owner has"""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's pet list"""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their name"""
        return sorted(self._pets, key=lambda pet: pet.name)
