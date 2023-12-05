from typing import Dict, Any


def process_data(data: Dict[str, Any]) -> None:
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")


# Example usage
data = {
    "name": "Jedi Master",
    "age": 900,
    "skills": ["Force", "Lightsaber"],
    "isJedi": True,
}

process_data(data)
