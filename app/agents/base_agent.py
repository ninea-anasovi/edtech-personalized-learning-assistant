from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute the agent's primary function."""
        pass