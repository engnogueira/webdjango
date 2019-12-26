import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'slug', [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_title_video(resp, slug):
    assert_contains(resp, slug)


@pytest.mark.parametrize(
    'slug', [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
#
#
# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/381369324"')
