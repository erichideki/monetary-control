import pytest
from rest_framework.test import APIClient
from finance.tests.factories.user_factory import UserFactory
from finance.tests.factories.account_factory import AccountFactory
from finance.tests.factories.category_factory import CategoryFactory
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def user():
    return UserFactory.create()

@pytest.fixture
def account(user):
    return AccountFactory.create(user=user)

@pytest.fixture
def category(user):
    return CategoryFactory.create(user=user)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def api_client_with_user(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def api_client_with_jwt():
    user = UserFactory.create()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return client, user