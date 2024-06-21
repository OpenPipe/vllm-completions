# Write an abstract class LoraModuleResolver that takes a method resolve lora

from abc import ABC, abstractmethod

class LoraModuleResolver(ABC):
    
    @abstractmethod
    def resolve_lora(self):
        """
        Abstract method to resolve and possibly download a Lora model on the fly.
        """
        pass