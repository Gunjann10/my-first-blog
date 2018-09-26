from django.shortcuts import render, get_object_or_404
from django.http import Http404
from music.models import album, song

def index(request):
    all_albums = album.objects.all()
    context = {'all_albums': all_albums}
    return render(request,'music/index.html' ,context)

def detail(request, album_id):
       #albums = album.objects.get(pk=album_id)
        albums = get_object_or_404(album, pk=album_id)
        return render(request,'music/detail.html',{'album' : albums})

def favorite(request, album_id):
      albums = get_object_or_404(album, pk= album_id)
      
      try:
          selected_song = albums.song_set.get(pk=request.POST['song'])
      except (KeyError, song.DoesNotExist):
          return render(request, 'music/detail.html', {'album' : albums ,
          'error_message': "You did not select a valid song"})
      else:
          selected_song.is_fav = True
          selected_song.save()
          return render(request, 'music/detail.html', {'album' : albums})
