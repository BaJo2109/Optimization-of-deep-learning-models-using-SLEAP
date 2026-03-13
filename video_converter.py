# %%
import subprocess
import os
import sys
import imageio_ffmpeg


INPUT_VIDEO = r"C:\Users\jrall\Desktop\Bachelorarbeit\Bachelor_Joschua\behavior_videos_maxim\1132\trial_2\video0030 25-01-24 19-53-50.mp4"
OUTPUT_VIDEO = r"C:\Users\jrall\Desktop\Bachelorarbeit\Bachelor_Joschua\behavior_videos_maxim\1132\trial_2\video0030 25-01-24 19-53-50_intra.mp4"
# ----------------------------------------

def convert_to_all_intra(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ Error: Input file not found: {input_path}")
        print("   -> Check the 'INPUT_VIDEO' path variable at the top of the script.")
        return

    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"🔧 Using ffmpeg located at: {ffmpeg_exe}")
    print(f"🎥 Input:  {input_path}")
    print(f"💾 Output: {output_path}")
    print("-" * 40)

    command = [
        ffmpeg_exe,
        "-y",
        "-i", input_path,
        "-g", "1",             
        "-c:v", "libx264",
        "-tune", "fastdecode",
        "-preset", "medium",
        "-crf", "15",
        "-pix_fmt", "yuv420p",
        "-loglevel", "error",
        "-stats",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print("-" * 40)
        print(f"✅ Success! New video saved to: {output_path}")
        print("\nNEXT STEPS:")
        print("1. Open SLEAP.")
        print("2. 'Videos' -> 'Replace Video'.")
        print("3. Select this new '_intra.mp4' file.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ FFmpeg failed with error code {e.returncode}.")

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        is_jupyter_junk = arg.startswith("-f") or arg.startswith("--f") or arg.endswith(".json")
        
        if not is_jupyter_junk:
            INPUT_VIDEO = arg
        else:
            print(f"⚠️ Detected Jupyter argument '{arg}'. Ignoring it and using hardcoded paths.")
    
    convert_to_all_intra(INPUT_VIDEO, OUTPUT_VIDEO)

# %%
!pip install imageio_ffmpeg