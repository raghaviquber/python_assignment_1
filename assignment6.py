songs_list=[]
list=input("Enter the duration of the songs in your playlist (in seconds) separated by commas: ")
list = list.replace("[", "").replace("]", "")
songs_list=list.split(",")
for i in range(len(songs_list)):
    songs_list[i] = int(songs_list[i].strip())
if any(int(i)<=0 for i in songs_list):
    print("Invalid entry")
else:
    total_duration=sum(songs_list)
    number_of_songs=len(songs_list)
    
    repetetive=False
    for i in songs_list:
        if songs_list.count(i)>1:
            repetetive=True
            break
    if total_duration<300:
        category="Too Short Playlist"
        recommendation="Add more songs to your playlist."
    elif total_duration>3600:
        category="Too Long Playlist"
        recommendation="Remove some songs from your playlist."
    elif repetetive:
        category="Repetitive Playlist"
        recommendation="Consider adding more variety to your playlist."
    elif (max(songs_list)-min(songs_list))>600:
        category="Irregular Playlist"
        recommendation="Try to have a more consistent song duration in your playlist."
    else:
        category="Balanced Playlist"
        recommendation="Your playlist is well balanced!"
    print("Total Duration: ",total_duration," seconds")
    print("Songs: ",number_of_songs)
    print("Category: ",category)
    print("Recommendation: ",recommendation)   