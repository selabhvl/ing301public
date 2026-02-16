class Dial:

    def __init__(self, start_value: int = 50) -> None:
        self.value = start_value

    def dial(self, instruction: str):
        """
        Expects dial instructions, e.g. `R10`, `L55`, ...
        which tell how many times the dial should be turned to the left or the right,
        Rhe dial is a circle, turning the dial left from 0 one click makes it point at 99.
        Similarly, turning the dial right from 99 one click makes it point at 0.
        """
        raise NotImplemented

    def obtain_password(self, instructions: list[str]):
        result = 0
        for i in instructions:
            self.dial(i)
            if self.value == 0:
                result += 1
        return result
        

