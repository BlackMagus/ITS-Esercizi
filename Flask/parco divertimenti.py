from abc import ABC, abstractmethod
import math

class Ride(ABC):
    def __init__(self, ride_id: str, name: str, min_height_cm: int):
        self.id = ride_id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category()
        }

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        base = self.base_wait()
        estimated = base * crowd_factor
        return max(0, math.ceil(estimated))


class RollerCoaster(Ride):
    def __init__(self, ride_id: str, name: str, min_height_cm: int, inversions: int):
        
        super().__init__(ride_id, name, min_height_cm)
        
        self.inversions = inversions
        
    
    def info(self) -> dict:
        data = super().info()
        data["inversions"] = self.inversions
        return data
