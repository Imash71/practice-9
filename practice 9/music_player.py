tracks = ["Track 1", "Track 2", "Track 3"]
current = 0
print("🎵 Music Player Started")
while True:
   print("\nNow playing:", tracks[current])
   print("P - Play | N - Next | B - Back | Q - Quit")
   cmd = input("Enter command: ").upper()
   if cmd == "P":
       print("▶ Playing:", tracks[current])
   elif cmd == "N":
       current = (current + 1) % len(tracks)
   elif cmd == "B":
       current = (current - 1) % len(tracks)
   elif cmd == "Q":
       print("Bye 👋")
       break
   else:
       print("Invalid command")