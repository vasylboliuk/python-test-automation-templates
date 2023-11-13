import dataclasses

from rest_api.placeholder_ms.model.user_model import UserDto


class TestDataclass:
    def test_user_dto(self):
        user_data = UserDto(
            id=10,
            name="Vasyl",
            username="vbol"
        )
        print(f"------------------------")
        print(f"Print UserDto object {user_data}\n")
        print(f"Print UserDto dict: {dataclasses.asdict(user_data)}\n")
        print(f"Print UserDto tuple: {dataclasses.astuple(user_data)}\n")
        print(f"Print UserDto object dict: {user_data.to_dict()}\n")
        print(f"Print UserDto custom dict: {user_data.as_dict()}\n")
        print(f"Print UserDto custom exclude None dict: {user_data.as_dict(exclude_none=True)}\n")
