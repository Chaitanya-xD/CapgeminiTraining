public interface IPlayable{
  void Play();
}

public class MusicPlayer : IPlayable{
  public void Play(){
    Console.WriteLine("Music Playing");
  }
}
public class VideoPlayer : IPlayable{
  public void Play(){
    Console.WriteLine("Video Playing");
  }
}

public class oop8{
  public static void main(string[] args){
    MusicPlayer music = new MusicPlayer();
    VideoPlayer video = new VideoPlayer();

    music.Play();
    video.Play();
  }

}