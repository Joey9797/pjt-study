# requests 사용 예시 2

import requests
from pprint import pprint
import sys

sys.path.append('..')
from config.spotify_config import getHeaders


def get_music():
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': 'artist:BTS',  # 필수 파라미터
        # 'q': 'artist:BTS track:Take Two',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.
    result = response.get('tracks').get('items')

    return result


if __name__ == '__main__':
    # 아티스트 BTS의 트랙 Take Two 정보를 조회
    pprint(get_music())
    """
    [{
        'album': {'album_type': 'single',
            'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6HaGTQPmzraVmaVxvz6EUc'},
                         'href': 'https://api.spotify.com/v1/artists/6HaGTQPmzraVmaVxvz6EUc',
                         'id': '6HaGTQPmzraVmaVxvz6EUc',
                         'name': 'Jung Kook',
                         'type': 'artist',
                         'uri': 'spotify:artist:6HaGTQPmzraVmaVxvz6EUc'},
                        {'external_urls': {'spotify': 'https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX'},
                         'href': 'https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX',
                         'id': '3Nrfpe0tUJi4K4DXYWgMUX',
                         'name': 'BTS',
                         'type': 'artist',
                         'uri': 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'}],
            'external_urls': {'spotify': 'https://open.spotify.com/album/6GnWToxHfF7hobSYdi5V8u'},
            'href': 'https://api.spotify.com/v1/albums/6GnWToxHfF7hobSYdi5V8u',
            'id': '6GnWToxHfF7hobSYdi5V8u',
            'images': [{'height': 640,
                        'url': 'https://i.scdn.co/image/ab67616d0000b273cfe3ffeee2f4ec0291f9d969',
                        'width': 640},
                       {'height': 300,
                        'url': 'https://i.scdn.co/image/ab67616d00001e02cfe3ffeee2f4ec0291f9d969',
                        'width': 300},
                       {'height': 64,
                        'url': 'https://i.scdn.co/image/ab67616d00004851cfe3ffeee2f4ec0291f9d969',
                        'width': 64}],
            'is_playable': True,
            'name': 'Dreamers [Music from the FIFA World Cup Qatar 2022 '
                    'Official Soundtrack]',
            'release_date': '2022-11-20',
            'release_date_precision': 'day',
            'total_tracks': 1,
            'type': 'album',
            'uri': 'spotify:album:6GnWToxHfF7hobSYdi5V8u'},
            'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6HaGTQPmzraVmaVxvz6EUc'},
                        'href': 'https://api.spotify.com/v1/artists/6HaGTQPmzraVmaVxvz6EUc',
                        'id': '6HaGTQPmzraVmaVxvz6EUc',
                        'name': 'Jung Kook',
                        'type': 'artist',
                        'uri': 'spotify:artist:6HaGTQPmzraVmaVxvz6EUc'},
                        {'external_urls': {'spotify': 'https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX'},
                        'href': 'https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX',
                        'id': '3Nrfpe0tUJi4K4DXYWgMUX',
                        'name': 'BTS',
                        'type': 'artist',
                        'uri': 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'},
                        {'external_urls': {'spotify': 'https://open.spotify.com/artist/5C01hDqpEmrmDfUhX9YWsH'},
                        'href': 'https://api.spotify.com/v1/artists/5C01hDqpEmrmDfUhX9YWsH',
                        'id': '5C01hDqpEmrmDfUhX9YWsH',
                        'name': 'FIFA Sound',
                        'type': 'artist',
                        'uri': 'spotify:artist:5C01hDqpEmrmDfUhX9YWsH'}],
            'disc_number': 1,
            'duration_ms': 201391,
            'explicit': False,
            'external_ids': {'isrc': 'QZNMY2232113'},
            'external_urls': {'spotify': 'https://open.spotify.com/track/0jY618wuln0b5b8sCxFgjk'},
            'href': 'https://api.spotify.com/v1/tracks/0jY618wuln0b5b8sCxFgjk',
            'id': '0jY618wuln0b5b8sCxFgjk',
            'is_local': False,
            'is_playable': True,
            'name': 'Dreamers [Music from the FIFA World Cup Qatar 2022 Official '
                    'Soundtrack]',
            'popularity': 72,
            'preview_url': None,
            'track_number': 1,
            'type': 'track',
            'uri': 'spotify:track:0jY618wuln0b5b8sCxFgjk'
    }]
    """
