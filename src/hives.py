from datetime import timedelta

class Hive:
    '''
    producing-bees
    season-start
    season-end
    storage-nectar
    has-seed?
    '''

    def __init__(self, age: int, species: str, producing_bees: bool, season_start: timedelta, 
    season_end: timedelta, storage_nectar: int, has_seed: bool):
        self.age = age
        self.species = species
        self.producing_bees = producing_bees
        self.season_start = season_start
        self.season_end = season_end
        self.storage_nectar = storage_nectar
        self.has_seed = has_seed

    # Age
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    # Species
    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    # Producing Bees
    @property
    def producing_bees(self) -> bool:
        return self._producing_bees

    @producing_bees.setter
    def producing_bees(self, value: bool) -> None:
        self._producing_bees = value

    # Season Start
    @property
    def season_start(self) -> timedelta:
        return self._season_start

    @season_start.setter
    def season_start(self, value: timedelta) -> None:
        self._season_start = value

    # Season End
    @property
    def season_end(self) -> timedelta:
        return self._season_end

    @season_end.setter
    def season_end(self, value: timedelta) -> None:
        self._season_end = value

    # Storage Nectar
    @property
    def storage_nectar(self) -> int:
        return self._storage_nectar

    @storage_nectar.setter
    def storage_nectar(self, value: int) -> None:
        self._storage_nectar = value

    # Has Seed
    @property
    def has_seed(self) -> bool:
        return self._has_seed

    @has_seed.setter
    def has_seed(self, value: bool) -> None:
        self._has_seed = value

    
    