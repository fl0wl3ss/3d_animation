# 
# 
#  
# ffmpeg -framerate 30 -i output_frames/frame_%04d.png -c:v libx264 -pix_fmt yuv420p output_frames/output.mp4
#
#
#
import os 
import subprocess
# FFmpegコマンドを指定
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '60',  # フレームレート
    '-i', 'output_frames/frame_%04d.png',  # 入力ファイル名のパターン
    '-c:v', 'libx264',  # 動画コーデックを指定
    '-pix_fmt', 'yuv420p',  # 色フォーマットを指定
    'output_frames/output.mp4'  # 出力ファイル名
]

# FFmpegコマンドを実行
subprocess.run(ffmpeg_command)
