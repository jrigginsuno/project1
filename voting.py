from typing import List, Tuple


class Vote:
    def __init__(self) -> None:
        """
        Method to set default values>
        """
        self.__candidates: Tuple[str, str, str] = ('Bianca', 'Edward', 'Felicia')
        self.__votes: List[int] = [0, 0, 0]

    def get_candidate(self, index: int) -> str:
        """
        Method to access name of candidate.
        :param index: Index of candidate.
        :return: Name of Candidate.
        """
        return self.__candidates[index]

    def get_vote(self, index: int) -> int:
        """
        Method to access the number of votes of a candidate
        :param index: Index of vote count.
        :return: Number of votes
        """
        return self.__votes[index]

    def get_total(self) -> int:
        """
        Method to add and return the total vote count between all candidates.
        :return: Total amount of votes.
        """
        return sum(self.__votes)

    def add_vote(self, index: int) -> None:
        """
        Method to add one vote to candidate with the given index.
        :param index: Index of candidate to cast vote to.
        """
        self.__votes[index] += 1
