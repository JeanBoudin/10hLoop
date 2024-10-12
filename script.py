import os
import subprocess
from moviepy.editor import ImageClip, AudioFileClip

# Durée de la vidéo en secondes (10 heures)
duration_in_seconds = 10 * 60 * 60

# Fonction pour boucler l'audio sur 10 heures avec ffmpeg
def loop_audio_ffmpeg(input_file, output_file, duration_in_seconds):
    try:
        # Commande ffmpeg pour boucler le fichier MP3 sur 10 heures
        subprocess.run([
            'ffmpeg', '-stream_loop', '-1', '-i', input_file, 
            '-t', str(duration_in_seconds), '-c', 'copy', output_file
        ], check=True)
        print(f"Le fichier audio {output_file} a bien été généré.")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la génération du fichier audio : {e}")
        exit(1)

# Chemins des fichiers d'entrée
mp3_file = "/app/input.mp3"  # Ton fichier MP3 monté dans le conteneur
png_file = "/app/image.png"  # Ton fichier PNG monté dans le conteneur

# Nom du fichier audio bouclé
looped_audio_file = "looped_audio.mp3"

# Boucler l'audio sur 10 heures
looped_audio_file = loop_audio_ffmpeg(mp3_file, looped_audio_file, duration_in_seconds)

# Vérifier si le fichier audio a été créé
if not os.path.exists(looped_audio_file):
    print(f"Le fichier {looped_audio_file} n'existe pas.")
    exit(1)

# Charger l'image PNG
image_clip = ImageClip(png_file, duration=duration_in_seconds)

# Charger l'audio bouclé
audio_clip = AudioFileClip(looped_audio_file)

# Associer l'audio à l'image
video = image_clip.set_audio(audio_clip)

# Exporter la vidéo finale
output_file = "/app/output/video.mp4"
video.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24)

print(f"Vidéo générée : {output_file}")
