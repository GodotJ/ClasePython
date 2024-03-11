
import lyrics

songs = {
    "Post Malone - Congratulations": lyrics.congratulations,
    "Travis Scott - Goosebumps": lyrics.goosebumps,
    "Future - Mask Off": lyrics.MaskOff,
    "Slipknot - Before I Forget": lyrics.beforeForget,
    "Nirvana - The Man Who Sold The World": lyrics.SoldTheWorld,
    "Mac Miller - Self Care": lyrics.selfCare,
    "Skillet - Awake and Alive": lyrics.awakeAlive,
    "Smash Mouth - All Star": lyrics.allStar,
    "Control Machete - Comprendes, Mendes?": lyrics.mendes,
    "Joji - Tick Tock": lyrics.tickTock, 
}

print("Lista de canciones:")
for i, song in enumerate(songs, 1):
    print(f"{i}. {song}")

option = int(input("Elige una canción (1-10): "))

if option < 1 or option > 10:
    print("Opción inválida")
else:
    songTitle = list(songs.keys())[option - 1]
    songLyrics = songs[songTitle]
    
    print(f"\nElejiste: '{songTitle}' Aqui tienes. \n --------------- {songTitle}--------------- \n{songLyrics}")