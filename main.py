"""
Facebook Page Automated Poster for Hindi Shayari
Generates images with Hindi Shayari and posts them to Facebook Page automatically.
"""

import os
import json
import random
import requests
import schedule
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Configuration
PAGE_ID = os.getenv('FACEBOOK_PAGE_ID', '992326403963839')
ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'EAA7vMs3yYxABQtyIYJN8QdnNbyX01ffUxqUesHjjgpZAfyGKoZC35AAi4TzWj312GT3uXBloTnVvFevVV36H6Mf75K1ZAL1yUufQzalYeiTHqCCRkIfWnRkVpus8cxHsrmjiP12mf2EAjZB6foz59pCoHzmA4OozdQJCY0hGtJZBJ45R4rAX0TlN0fooiMx62hQcw')
WATERMARK_TEXT = "@ShayriCentre"  # Change this to your actual page name
FONT_PATH = "fonts/Lohit-Devanagari.ttf"  # Default font path
SHAYARIS_FILE = "shayaris.json"
OUTPUT_DIR = "output"
IMAGE_SIZE = (1080, 1080)  # Square image for Instagram/Facebook

# Posting interval with jitter (to avoid spam detection)
BASE_INTERVAL_MINUTES = 5  # Base interval: 5 minutes
JITTER_MINUTES = 2  # Random variation: ±2 minutes (posts between 3-7 minutes)

# Dark aesthetic color schemes
COLOR_SCHEMES = [
    {"bg": (18, 18, 18), "text": (255, 255, 255)},  # Pure black background
    {"bg": (26, 26, 46), "text": (255, 255, 255)},  # Dark blue
    {"bg": (30, 30, 30), "text": (240, 240, 240)},  # Dark gray
    {"bg": (20, 25, 35), "text": (255, 255, 255)},  # Dark navy
    {"bg": (25, 25, 25), "text": (220, 220, 220)},  # Charcoal
]


def load_shayaris():
    """Load Hindi Shayaris from JSON file."""
    try:
        with open(SHAYARIS_FILE, 'r', encoding='utf-8') as f:
            shayaris = json.load(f)
        return shayaris
    except FileNotFoundError:
        print(f"Error: {SHAYARIS_FILE} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {SHAYARIS_FILE}!")
        return []


def get_random_shayari():
    """Get a random Shayari from the list."""
    shayaris = load_shayaris()
    if not shayaris:
        return "ज़िंदगी की हर कहानी में, दर्द का एक अध्याय होता है।"
    return random.choice(shayaris)


def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = font.getbbox(test_line)
        text_width = bbox[2] - bbox[0]
        
        if text_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines


def generate_shayari_image(text):
    """
    Generate a 1080x1080 image with Hindi Shayari text.
    
    Args:
        text (str): The Hindi Shayari text to display
        
    Returns:
        str: Path to the generated image file
    """
    # Create output directory if it doesn't exist
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    
    # Select random color scheme
    colors = random.choice(COLOR_SCHEMES)
    
    # Create image with dark background
    img = Image.new('RGB', IMAGE_SIZE, color=colors['bg'])
    draw = ImageDraw.Draw(img)
    
    # Try to load font, fallback to default if not found
    try:
        # Adjust font size based on text length
        base_font_size = 60
        if len(text) > 80:
            base_font_size = 50
        elif len(text) > 120:
            base_font_size = 40
            
        try:
            font = ImageFont.truetype(FONT_PATH, base_font_size)
        except (OSError, IOError):
            print(f"Warning: Font {FONT_PATH} not found. Using default font.")
            font = ImageFont.load_default()
    except Exception as e:
        print(f"Warning: Could not load font. Using default. Error: {e}")
        font = ImageFont.load_default()
    
    # Calculate text dimensions and wrap text
    padding = 100
    max_width = IMAGE_SIZE[0] - (2 * padding)
    lines = wrap_text(text, font, max_width)
    
    # Calculate total text height
    line_height = font.getbbox('A')[3] - font.getbbox('A')[1] + 20
    total_height = len(lines) * line_height
    
    # Center text vertically
    start_y = (IMAGE_SIZE[1] - total_height) // 2
    
    # Draw each line of text
    y_position = start_y
    for line in lines:
        bbox = font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x_position = (IMAGE_SIZE[0] - text_width) // 2
        draw.text((x_position, y_position), line, fill=colors['text'], font=font)
        y_position += line_height
    
    # Add watermark at the bottom
    try:
        watermark_font_size = 24
        try:
            watermark_font = ImageFont.truetype(FONT_PATH, watermark_font_size)
        except (OSError, IOError):
            watermark_font = ImageFont.load_default()
    except Exception:
        watermark_font = ImageFont.load_default()
    
    watermark_bbox = watermark_font.getbbox(WATERMARK_TEXT)
    watermark_width = watermark_bbox[2] - watermark_bbox[0]
    watermark_x = (IMAGE_SIZE[0] - watermark_width) // 2
    watermark_y = IMAGE_SIZE[1] - 60
    draw.text((watermark_x, watermark_y), WATERMARK_TEXT, 
              fill=(150, 150, 150), font=watermark_font)
    
    # Save image with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/shayari_{timestamp}.jpg"
    img.save(filename, 'JPEG', quality=95)
    
    print(f"Image generated: {filename}")
    return filename


def upload_to_facebook(image_path, message=""):
    """
    Upload image to Facebook Page using Graph API.
    
    Args:
        image_path (str): Path to the image file
        message (str): Optional caption for the post
        
    Returns:
        bool: True if successful, False otherwise
    """
    if PAGE_ID == 'YOUR_PAGE_ID_HERE' or ACCESS_TOKEN == 'YOUR_ACCESS_TOKEN_HERE':
        print("Error: Please set FACEBOOK_PAGE_ID and FACEBOOK_ACCESS_TOKEN!")
        return False
    
    try:
        # Step 1: Upload photo to Facebook
        url = f"https://graph.facebook.com/v18.0/{PAGE_ID}/photos"
        
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            data = {
                'message': message,
                'access_token': ACCESS_TOKEN
            }
            
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            
            result = response.json()
            if 'id' in result:
                print(f"Successfully posted to Facebook! Post ID: {result['id']}")
                return True
            else:
                print(f"Error: Unexpected response from Facebook: {result}")
                return False
                
    except requests.exceptions.RequestException as e:
        print(f"Error uploading to Facebook: {e}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_detail = e.response.json()
                print(f"Facebook API Error Details: {error_detail}")
            except:
                print(f"Response Status: {e.response.status_code}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def post_shayari():
    """Main function to generate and post a Shayari."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting posting process...")
    
    try:
        # Get random Shayari
        shayari_text = get_random_shayari()
        print(f"Selected Shayari: {shayari_text[:50]}...")
        
        # Generate image
        image_path = generate_shayari_image(shayari_text)
        
        # Post to Facebook
        success = upload_to_facebook(image_path, message=shayari_text)
        
        if success:
            print("Posting completed successfully!")
        else:
            print("Posting failed, but image was saved.")
            
    except Exception as e:
        print(f"Error in post_shayari: {e}")
        import traceback
        traceback.print_exc()


def schedule_next_post():
    """Schedule the next post with random jitter to avoid spam detection."""
    # Calculate random interval with jitter
    # Base interval ± jitter (e.g., 5 minutes ± 2 minutes = 3-7 minutes)
    interval_minutes = BASE_INTERVAL_MINUTES + random.uniform(-JITTER_MINUTES, JITTER_MINUTES)
    interval_seconds = int(interval_minutes * 60)
    
    # Schedule the post
    schedule.clear()  # Clear any existing schedules
    schedule.every(interval_seconds).seconds.do(post_and_reschedule)
    
    next_post_time = datetime.now().timestamp() + interval_seconds
    next_post_datetime = datetime.fromtimestamp(next_post_time)
    
    print(f"Next post scheduled in {interval_minutes:.1f} minutes ({interval_seconds} seconds)")
    print(f"Next post time: {next_post_datetime.strftime('%Y-%m-%d %H:%M:%S')}")


def post_and_reschedule():
    """Post a Shayari and schedule the next one with jitter."""
    post_shayari()
    schedule_next_post()  # Reschedule with new random interval


def main():
    """Main function to set up scheduling and run the bot."""
    print("=" * 60)
    print("Hindi Shayari Facebook Auto-Poster")
    print("=" * 60)
    print(f"Page ID: {PAGE_ID}")
    print(f"Posting interval: {BASE_INTERVAL_MINUTES} minutes ± {JITTER_MINUTES} minutes")
    print(f"  (Random interval: {BASE_INTERVAL_MINUTES - JITTER_MINUTES}-{BASE_INTERVAL_MINUTES + JITTER_MINUTES} minutes)")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)
    
    # Check if shayaris file exists
    if not os.path.exists(SHAYARIS_FILE):
        print(f"Warning: {SHAYARIS_FILE} not found!")
        return
    
    # Post immediately on startup (optional - comment out if not needed)
    print("\nPosting first Shayari now...")
    post_shayari()
    
    # Schedule the next post with jitter
    schedule_next_post()
    
    print("\nScheduler started with jitter to avoid spam detection.")
    print("Press Ctrl+C to stop.\n")
    
    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nStopping scheduler...")
        print("Goodbye!")


if __name__ == "__main__":
    main()
