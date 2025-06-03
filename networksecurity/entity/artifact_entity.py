from dataclasses import dataclass

@dataclass #its like a decorator where

class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str