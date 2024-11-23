import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from typing import Dict, List, Optional


class SpotifyBPMFinder:
    def __init__(self, client_id: str, client_secret: str):
        """Initialize Spotify client with credentials."""
        self.sp = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret
            )
        )

    def get_track_info(self, track_name: str) -> Optional[Dict]:
        """Search for a track and get its information."""
        try:
            # Search for the track
            results = self.sp.search(q=track_name, type='track', limit=1)

            if not results['tracks']['items']:
                print(f"No results found for: {track_name}")
                return None

            track = results['tracks']['items'][0]

            # Get audio features which includes tempo (BPM)
            audio_features = self.sp.audio_features(track['id'])[0]

            return {
                'name': track['name'],
                'artists': [artist['name'] for artist in track['artists']],
                'bpm': round(audio_features['tempo']),
                'spotify_url': track['external_urls']['spotify']
            }
        except Exception as e:
            print(f"Error processing {track_name}: {str(e)}")
            return None


def read_tracks_from_file(filename: str) -> List[str]:
    """Read track names from a text file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


def main():
    # Direct assignment of credentials
    client_id = 'enter_your_Client_ID'
    client_secret = 'enter_your_Client_SECRET'

    # Initialize the BPM finder
    bpm_finder = SpotifyBPMFinder(client_id, client_secret)

    # Read tracks from mixer.txt
    tracks = read_tracks_from_file('C:/dj/mixers.txt')

    # Store all track information
    track_info_list = []
    print("\nFetching track information...\n")

    for track_name in tracks:
        info = bpm_finder.get_track_info(track_name)
        if info:
            track_info_list.append(info)

    # Sort tracks by BPM
    sorted_tracks = sorted(track_info_list, key=lambda x: x['bpm'])

    # Print sorted results
    print("\nTracks sorted by BPM (ascending):\n")
    print("{:<5} {:<50} {:<30} {:<10}".format("No.", "Track Name", "Artist(s)", "BPM"))
    print("-" * 95)

    for index, info in enumerate(sorted_tracks, 1):
        artists = ", ".join(info['artists'])
        print("{:<5} {:<50} {:<30} {:<10}".format(
            index,
            info['name'][:47] + "..." if len(info['name']) > 47 else info['name'],
            artists[:27] + "..." if len(artists) > 27 else artists,
            info['bpm']
        ))

    # Print summary statistics
    print("\nSummary:")
    print(f"Lowest BPM: {sorted_tracks[0]['bpm']} ({sorted_tracks[0]['name']})")
    print(f"Highest BPM: {sorted_tracks[-1]['bpm']} ({sorted_tracks[-1]['name']})")
    print(f"Average BPM: {round(sum(track['bpm'] for track in sorted_tracks) / len(sorted_tracks), 1)}")


if __name__ == "__main__":
    main()
