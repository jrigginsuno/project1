from typing import List, Tuple
import csv
import os


class Vote:
    def __init__(self) -> None:
        """
        Method to set default values
        """
        self.__candidates: Tuple[str, str, str] = ('Bianca', 'Edward', 'Felicia')
        self.__votes: List[int] = [0, 0, 0]
        self.__csv_file = 'votes.csv'
        self.__create_csv_file()

    def __create_csv_file(self) -> None:
        """
        Method to create the CSV file if it doesn't exist or overwrite it if it does.
        """
        if os.path.exists(self.__csv_file):
            os.remove(self.__csv_file)
        with open(self.__csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['VoterID', 'Candidate'])

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
        
    def check_unique_voter_id(self, voter_id: str) -> bool:
        """
        Method to check if the voter ID is unique.
        :param voter_id: Voter ID to be checked.
        :return: True if the voter ID is unique, False otherwise.
        """
        with open('votes.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == voter_id:
                    return False
        return True

    def save_vote(self, voter_id: str, candidate_index: int) -> None:
        """
        Method to save the vote along with the voter ID and candidate name to a CSV file.
        :param voter_id: Voter ID.
        :param candidate_index: Index of the selected candidate.
        """
        candidate_name = self.get_candidate(candidate_index)
        with open(self.__csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate_name])

