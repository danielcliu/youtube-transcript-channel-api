from unittest import TestCase
from unittest.mock import patch

import json
import os
import requests

from .helpers import make_response, load_json
from youtube_transcript_channel_api.transcripts import YoutubePlaylistTranscripts
from youtube_transcript_channel_api.tes import hello

class TestYoutubePlaylistTranscripts(TestCase):
    base_package = __module__.split('.')[0]

    def test_back(self):
        self.assertEqual(True, True)

    @patch(f'{base_package}.transcripts.requests.get', return_value=make_response('jBnWZijMbMY_YDAPI_response.json'))
    def test_get_playlist_videos(self, mock_api_get):
        getter = YoutubePlaylistTranscripts('test', 'playlist_id', 'key')
        mock_api_get.assert_called_once()
        assert len(getter.video) == 7 

    @patch(f'{base_package}.transcripts.YouTubeTranscriptApi.get_transcript', return_value=load_json('jBnWZijMbMY_YTA_response.json'))
    @patch(f'{base_package}.transcripts.requests.get', return_value=make_response('jBnWZijMbMY_YDAPI_response.json'))
    def test_get_transcript(self, mock_api_get, mock_ytapi):
        getter = YoutubePlaylistTranscripts('test', 'playlist_id', 'key')
        mock_api_get.assert_called_once()
        res = getter._get_transcript(('test', 'title'), [], ['en'], None, None, False)
        mock_ytapi.assert_called_once()
        assert len(res) == 1

    @patch(f'{base_package}.transcripts.YoutubePlaylistTranscripts._get_transcript', return_value={'testing': 'value'})
    @patch(f'{base_package}.transcripts.requests.get', return_value=make_response('jBnWZijMbMY_YDAPI_response.json'))
    def test_get_transcripts(self, mock_api_get, mock_get_transcript):
        getter = YoutubePlaylistTranscripts('test', 'playlist_id', 'key')
        mock_api_get.assert_called_once()
        res, errors = getter.get_transcripts()
        mock_get_transcript.assert_called()
        assert len(res) == 1
        assert len(errors) == 0 
        
    @patch(f'{base_package}.hello.helloworld', return_value = 'ok')
    def test_hello(self, mock_hello):
        x = hello()
        print(x.helloworld())
        assert True 
