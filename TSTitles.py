
# Title translation

# Songs belong to Taylor Swift, pls don't sue me, I didn't step on your lawn 



albums = {
    "Taylor Swift": ["Tim McGraw", "Picture to Burn", "Teardrops on My Guitar", "A Place in This World",
                     "Cold as You", "The Outside", "Tied Together with a Smile", "Stay Beautiful",
                     "Should've Said No", "Mary's Song", "Our Song", "I'm Only Me When I'm With You",
                     "Invisible", "A Perfectly Good Heart"],
    "Beautiful Eyes": ["Beautiful Eyes", "I Heart?"],
    "Fearless": ["Fearless", "Fifteen", "Love Story", "Hey Stephen", "White Horse",
                 "You Belong with Me", "Breathe", "Tell Me Why", "You're Not Sorry",
                 "The Way I Loved You", "Forever & Always", "The Best Day", "Change",
                 "Jump Then Fall", "Untouchable", "Come In with the Rain", "Superstar",
                 "The Other Side of the Door", "Today Was a Fairytale", "You All Over Me",
                 "Mr. Perfectly Fine", "We Were Happy", "That's When", "Don't You", "Bye Bye Baby"],
    "Speak Now": ["Mine", "Sparks Fly", "Back to December", "Speak Now", "Dear John", "Mean",
                  "The Story of Us", "Never Grow Up", "Enchanted", "Better than Revenge", "Innocent",
                  "Haunted", "Last Kiss", "Long Live", "Ours", "Superman", "Electric Touch",
                  "When Emma Falls in Love", "I Can See You", "Castles Crumbling", "Foolish One", "Timeless"],
    "Red": ["State of Grace", "Red", "Treacherous", "I Knew You Were Trouble", "All Too Well", "22",
            "I Almost Do", "We Are Never Ever Getting Back Together", "Stay Stay Stay", "The Last Time",
            "Holy Ground", "Sad Beautiful Tragic", "The Lucky One", "Everything Has Changed", "Starlight",
            "Begin Again", "The Moment I Knew", "Come Back... Be Here", "Girl at Home", "Ronan", "Better Man",
            "Message in a Bottle", "I Bet You Think About Me", "Forever Winter", "Run", "The Very First Night"],
    "1989": ["Welcome to New York", "Blank Space", "Style", "Out of the Woods", "All You Had to Do Was Stay",
             "Shake It Off", "I Wish You Would", "Bad Blood", "Wildest Dreams", "How You Get the Girl",
             "This Love", "I Know Places", "Clean", "Wonderland", "You Are In Love", "New Romantics", "Slut!",
             "Say Don't Go", "Now That We Don't Talk", "Suburban Legends", "Is It Over Now?"],
        "reputation": ["...Ready for It?", "End Game", "I Did Something Bad", "Don't Blame Me", "Delicate",
                       "Look What You Made Me Do", "So It Goes...", "Gorgeous", "Getaway Car", "King of My Hear",
                       "Dancing with Our Hands Tied", "Dress", "This Is Why We Can't Have Nice Things",
                       "Call It What You Want", "New Year's Day"],
        "Lover": ["I Forgot That You Existed", "Cruel Summer", "Lover", "The Man", "The Archer",
                  "I Think He Knows", "Miss Americana & the Heartbreak Prince", "Paper Rings", 
                  "Cornelia Street", "Death by a Thousand Cuts", "London Boy", "Soon You'll Get Better",
                  "False God", "You Need to Calm Down", "Afterglow" "Me!", "It's Nice to Have a Friend", "Daylight"],
        "folklore": ["The 1", "Cardigan", "The Last Great American Dynasty", "Exile",
                     "My Tears Ricochet", "Mirrorball", "Seven", "August", "This is me trying", 
                     "illicit affairs", "invisible string", "mad woman", "epiphany", "betty",
                     "peace", "hoax", "the lakes"],
        "evermore": ["willow", "champagne problems", "gold rush", "'tis the damn season", "tolerate it",
                     "no body, no crime", "happiness", "dorothea", "coney island", "ivy", "cowboy like me",
                     "long story short", "marjorie", "closure", "evermore", "right where you left me", "it's time to go"],
        "Midnights": ["Lavender Haze", "Maroon", "Anti-Hero", "Snow on the Beach", "You're on Your Own, Kid", "Midnight Rain",
                      "Question...?", "Vigilante Shit", "Bejeweled", "Labyrinth", "Karma", "Sweet Nothing", "Mastermind",
                      "Hits Different", "The Great War", "Bigger Than the Whole Sky", "Paris", "High Infidelity", "Glitch",
                      "Would've, Could've, Should've", "Dear Reader", "You're Losing Me"],
        "The Tortured Poets Department": ["Fortnight", "The Tortured Poets Department", "My Boy Only Breaks His Favorite Toys",
                        "Down Bad", "So Long, London", "But Daddy I Love Him", "Fresh Out the Slammer", "Florida!!!", "Guilty as Sin?",
                        "Who's Afraid of Little Old Me?", "I Can Fix Him", "loml", "I Can Do It with a Broken Heart",
                        "The Smallest Man Who Ever Lived", "The Alchemy", "Clara Bow", "The Black Dog", "imgonnagetyouback",
                        "The Albatross", "Chloe or Sam or Sophia or Marcus", "How Did It End?", "So High School", "I Hate It Here",
                        "Thank You Aimee", "I Look in People's Windows", "The Prophecy", "Cassandra", "Peter", "The Bolter", "Robin", "The Manuscript"]
        

}


lowercase_albums = {k.lower(): [song.lower() for song in v] for k, v in albums.items()}
print("Hello user to the Taylor Swift discorgraphy! You chose an album, I give you the songs!")
album_choice = input("Chose an album: ").strip().lower()

if album_choice in lowercase_albums:
    print(f"Songs in the album '{album_choice}':")
    for song in lowercase_albums[album_choice]:
        print(f"- {song}")