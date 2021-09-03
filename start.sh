echo "Cloning Repo...."
git clone https://github.com/LushaiMusic/VCMusicPlayer.git /VCMusicPlayer
cd /VCMusicPlayer
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
