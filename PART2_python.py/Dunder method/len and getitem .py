class Playlist:
    def __init__(self):
        self.song = []

    def Add(self, song):
        self.song.append(song)
    def __len__(self):
        return len(self.song)

# Create Playlist object
p = Playlist()

# Add songs
p.Add("Believer")
p.Add("Shape of You")
p.Add("Perfect")

# Display playlist
print(p.song)
print(len(p))