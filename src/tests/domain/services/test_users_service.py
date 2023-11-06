import unittest
from unittest.mock import Mock
from app.data_access.DTOs.user_dto import UserDto
from app.domain.services.users_service import UsersService
from app.domain.entities.user import User

class UserServiceTest(unittest.TestCase):
    def test_get_all_users(self):
        mock_repository = Mock()
        mock_repository.getAll.return_value = [UserDto(user_id=1, name='Alice'),UserDto(user_id=2, name='Bob'),UserDto(user_id=3, name='Charlie')]
        expectedResult = [User(id=1,name='Alice'),User(id=2,name='Bob'),User(id=3,name='Charlie')]
        
        sut = UsersService(mock_repository)
        result = sut.getAll()
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()